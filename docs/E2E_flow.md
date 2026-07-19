```text 
USER SENDS A QUESTION
        |
        v
ChatService receives:
- question
- repo_url
- conversation_id
        |
        v
Load Short-Term Memory
- Get the latest 8 chat messages
        |
        v
Load Long-Term Memory
- Get saved user facts for this conversation
- Example: "User prefers Python examples"
        |
        v
START HYBRID RETRIEVAL
        |
        v
Find the repository ID using repo_url
        |
        +--> Repository is not indexed?
        |          |
        |          v
        |    Context = "Repository has not been indexed."
        |
        +--> Repository is indexed
                   |
                   v
          VECTOR RETRIEVAL
          - Convert the current question into an embedding
          - Compare it with stored code-chunk embeddings
          - Select the top 3 most similar code chunks
                   |
                   v
          EXTRACT ENTITIES
          - Read the selected code chunks
          - Extract names such as classes or functions
                   |
                   v
          GRAPH RETRIEVAL
          - Load the repository graph, if it exists
          - Search graph nodes using extracted entities
          - Find related code structure/information
                   |
                   v
          BUILD REPOSITORY CONTEXT
          - Combine vector-search results
          - Combine graph-search results
                   |
                   v
        HYBRID REPOSITORY CONTEXT READY
        |
        v
Build One Prompt for the AI
- Short-term history: recent conversation
- Long-term memory: lasting user facts
- Hybrid repository context: relevant code and graph data
- Current question
        |
        v
AI GENERATES ANSWER
        |
        v
Save Short-Term Memory
- Save current user question
- Save current assistant answer
        |
        v
Process Long-Term Memory
- Send this question-and-answer pair to the memory extractor
        |
        v
Gemini decides whether it contains a useful lasting fact
        |
        +--> No useful fact
        |          |
        |          v
        |      Save nothing
        |
        +--> Useful fact found
                   |
                   v
          Save each fact in the database:
          - conversation_id
          - fact
                   |
                   v
          RETURN ANSWER TO USER

```