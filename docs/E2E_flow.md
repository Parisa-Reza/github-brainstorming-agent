# End-to-End Flow: Repository Chat and GitHub MCP

This document describes the current flow after GitHub MCP support and
repository-scoped memory were added.

## 1. Load a repository

```text
USER PASTES A GITHUB REPOSITORY URL
        |
        v
Browser POSTs github_url to Django
        |
        v
RepositoryIngestionWorkflow.ingest(repo_url)
        |
        v
Create an owner-scoped local path
data/repositories/<owner>/<repository>
        |
        +--> Checkout already exists?
        |          |
        |          +--> Yes: reuse that checkout
        |          |
        |          +--> No: clone the repository from GitHub
        |
        v
Discover supported source and documentation files
        |
        v
Load file contents into repository documents
        |
        v
Split documents into chunks
        |
        v
Generate an embedding for every chunk
        |
        v
Find or create the database repository record by the exact repo_url
        |
        v
Delete that repository record's old chunks
        |
        v
Store the new chunks with that repository_id
        |
        v
Save repo_url as the browser session's Active Repository
Clear the visible browser chat
        |
        v
Redirect to the chat page
```

The owner-scoped checkout prevents repositories owned by different GitHub
accounts from sharing a local directory. Replacing old chunks prevents stale
code from appearing after a repository is loaded again.

## 2. Ask a question

```text
USER SENDS A QUESTION
        |
        v
Browser POSTs question to Django
        |
        v
Read the Active Repository URL from the browser session
        |
        +--> No active repository?
        |          |
        |          v
        |    Return JSON error: load a repository first
        |
        +--> Active repository exists
                   |
                   v
          ChatService receives:
          - question
          - repo_url
          - browser session id
                   |
                   v
          Create a repository-scoped memory key
          browser session id + hash(repo_url)
                   |
                   v
          Load the latest 8 messages for this repository only
                   |
                   v
          Parse repo_url into GitHub owner and repository
                   |
                   v
          MCPRouter checks the question
                   |
          +--------+-----------------------------------------+
          |        |                                         |
          v        v                                         v
   MCP QUESTION?    NO                                Yes, MCP question
          |                                                  |
          |                                                  v
          |                                         Call GitHub MCP server
          |                                                  |
          |                           +----------------------+---------------------+
          |                           |                      |                     |
          |                           v                      v                     v
          |                     README request        Branch/PR request      Commit request
          |                     get_file_contents     list_branches /        list_commits
          |                                             list_pull_requests          |
          |                                                                         |
          |                                              Commit-details request?    |
          |                                                                         |
          |                                            list commits -> find SHA -> get_commit
          |                                                                         |
          |                                                                         v
          |                                         Format live GitHub result:
          |                                         message, author, date, files,
          |                                         additions/deletions, diff when available
          |                                                  |
          |                                                  v
          |                                         Save question and answer in
          |                                         this repository's short-term memory
          |                                                  |
          |                                                  v
          |                                         Return JSON answer to browser
          |
          v
   Load this repository's long-term memory
          |
          v
   START HYBRID RETRIEVAL
          |
          v
   Find the database repository_id using the exact repo_url
          |
          +--> Repository is not indexed?
          |          |
          |          v
          |    Context = "Repository has not been indexed."
          |
          +--> Repository is indexed
                     |
                     v
            Vector retrieval
            - embed the question
            - read chunks WHERE repository_id = active repository_id
            - calculate similarity
            - select the best 3 chunks
                     |
                     v
            Extract entities from those chunks
            - classes, functions, identifiers, and related terms
                     |
                     v
            Graph retrieval, if the active repository graph exists
            - load data/repositories/<owner>/<repository>/graphify-out/graph.json
            - find nodes related to the extracted entities
                     |
                     v
            Build hybrid repository context
            - vector chunks
            - graph nodes
                     |
                     v
   Build the LLM prompt
   - repository-scoped short-term history
   - repository-scoped long-term memory
   - hybrid context for the active repository only
   - current question
          |
          v
   LLM generates the answer
          |
          v
   Save question and answer in this repository's short-term memory
          |
          v
   Process long-term memory
          |
          +--> No useful long-term fact? --> Save nothing
          |
          +--> Useful fact found? -------> Save it under this repository's memory key
          |
          v
   Return JSON answer to browser
          |
          v
Browser renders Markdown and syntax-highlights code blocks
```

## 3. What happens in parallel?

The current implementation is mostly **sequential**, not parallel:

```text
Current request path

MCP route:       route -> GitHub MCP call(s) -> format -> save memory -> response
Hybrid route:    load memory -> vector retrieval -> entity extraction -> graph retrieval
                 -> LLM -> save memory -> long-term-memory extraction -> response
```

The two branches are alternatives, not simultaneous work for one question:

```text
                  MCP question? yes  --> GitHub MCP branch only
Question routing
                  MCP question? no   --> Hybrid retrieval + LLM branch only
```

This is intentional. A live GitHub answer, such as a latest commit, should not
be mixed with retrieved local code chunks or rewritten by the LLM.

Separate browser tabs may send requests at the same time, and loading a
repository can happen while another user/session is using the application.
However, within one request the code does not currently run clone, embedding,
MCP calls, vector retrieval, graph retrieval, or memory extraction in parallel.

## 4. Memory isolation when multiple repositories are loaded

```text
One browser session
|
+-- session id + hash(Repo A URL) --> Repo A history and long-term memory
|
+-- session id + hash(Repo B URL) --> Repo B history and long-term memory
|
`-- session id + hash(Repo C URL) --> Repo C history and long-term memory
```

Changing the Active Repository clears the visible chat. More importantly, the
server changes the memory key, so a previous answer about Repo A cannot be
included in Repo B's prompt.
