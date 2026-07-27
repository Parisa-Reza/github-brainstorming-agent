# GitHub Brainstorming Agent

**Live Link:** [Demo video of the agent](<https://1drv.ms/v/c/a1e09615c8a551ad/IQDwsnb8B68gTZ05OG1w2ML8Ae8ndutiDUTWjO8TUOqmdQU?e=bRKATR>)

**Demo Video 1 :**  [Demo video of the agent](<https://1drv.ms/v/c/a1e09615c8a551ad/IQDwsnb8B68gTZ05OG1w2ML8Ae8ndutiDUTWjO8TUOqmdQU?e=bRKATR>)
<br>
**Demo Video 2 :**  [Demo video of the agent working as an MCP server with Crew AI](<https://1drv.ms/v/c/a1e09615c8a551ad/IQDc4sa2nn2EQaBg31-b0laVAYc4wsLNNqTuP9VCfG99KR8?e=95KDSW>)

---

## Project Description

Built an agent using LangChain, Hybrid RAG, SurrealDB memory, and GitHub MCP tools, Django, capable of answering repository-specific questions through vector search, graph retrieval, and live GitHub metadata. 
The project also exposes itself as an MCP (Model Context Protocol) server so that other AI agents can communicate with it using standardized Agent-to-Agent (A2A) communication.

<img width="2012" height="2212" alt="image" src="https://github.com/user-attachments/assets/62997431-8942-49ba-9c4f-bc0b8d584228" />



---

## Features

* Chat with any public GitHub repository
* Hybrid Retrieval (Vector Search + Graph Search)
* Live GitHub repository information through MCP
* Repository-aware conversations
* Long-term memory using SurrealDB
* Agent-to-Agent communication through MCP
* Django web interface

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Django | Backend framework and web interface |
| LangChain | AI orchestration and RAG pipeline |
| Google Gemini | Large Language Model |
| Sentence Transformers | Text embeddings|
| Graphfy | Knowledge graphs|
| SurrealDB | Long-term memory and short-term memory |
| GitHub MCP Server | Live GitHub repository access |
| Official MCP Python SDK | Standardized communication between AI agents |
| Hybrid RAG | Combines vector search and graph retrieval |
| Git | Version control |

---



## System Architecture

```text
                               External AI Agent
                         (CrewAI, LangGraph, etc.)
                                      │
                                      │ MCP Client
                                      ▼
                     GitHub Engineering Mentor MCP Server
                                      │
                                      ▼
+--------------------------------------------------------------------------------+
|                              GitHub Engineering Mentor                         |
|                                                                                |
|  User                                                                          |
|    │                                                                           |
|    ▼                                                                           |
|  Django Web Interface                                                          |
|    │                                                                           |
|    ▼                                                                           |
|  Chat Service                                                                  |
|    │                                                                           |
|    ├──────────────► Conversation History                                       |
|    │                                                                           |
|    ├──────────────► Memory Manager                                             |
|    │                  ├── Short-term Memory  (SurrealDB)                                    |
|    │                  └── Long-term Memory (SurrealDB)                         |
|    │                                                                           |
|    ├──────────────► Hybrid Retrieval                                           |
|    │                  ├── Vector Search                                        |
|    │                  └── Graph Search                                         |
|    │                                                                           |
|    ├──────────────► GitHub MCP Service                                         |
|    │                  ├── Repository Metadata                                  |
|    │                  ├── Commit History                                       |
|    │                  └── Pull Requests                                        |
|    │                                                                           |
|    │                                                                           |
|    │                                                                           |
|    ├──────────────► Context Builder                                            |
|    │                  │                                                        |
|    │                  ├── Hybrid Retrieval Context                             |
|    │                  ├── Memory Context                                       |
|    │                  ├── GitHub MCP Context                                   |
|    │                  └── Conversation Context                                 |
|    │                                                                           |
|    ▼                                                                           |
|  Gemini LLM (LangChain)                                                        |
|    │                                                                           |
|    ▼                                                                           |
|  Final Response                                                                |
+--------------------------------------------------------------------------------+
```




---

## How It Works


1. The user paste a repository URL and  asks a question from the Django web application.
2. The chat service collects useful information from multiple sources.
3. The Hybrid Retrieval system searches both vector embeddings and the repository knowledge graph.
4. The Memory Manager provides short-term conversation history and long-term memories stored in SurrealDB.
5. The GitHub MCP Service fetches live repository information such as files, commits, branches, pull requests, and code search results.
6. The Context Builder combines all retrieved information into a single prompt.
7. LangChain sends the complete context to the Gemini model.
8. The model generates a repository-aware answer and returns it to the user.
9. The same mentor is also exposed as an MCP server, allowing external AI agents to communicate with it through standard MCP clients for A2A collaboration.



---
## Tables in Surrealdb
```
SurrealDB
│
├── repository      ← Repository metadata
│
├── chunk           ← RAG chunks + embeddings
│
├── conversation    ← Short-term memory
│
└── memory          ← Long-term memory
```


---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Parisa-Reza/github-brainstorming-agent.git

cd github-brainstorming-agent
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your_secret_key

DEBUG=True

GEMINI_API_KEY=your_gemini_api_key

SURREAL_URL=ws://localhost:8001

SURREAL_USERNAME=root

SURREAL_PASSWORD=root

SURREAL_NAMESPACE=mentor

SURREAL_DATABASE=memory

GITHUB_TOKEN=github_pat_token
```

---


### 5. Start SurrealDB

The project already includes a `docker-compose.yml`.

Start the database with:

```bash
docker compose up -d
```

Verify that the container is running:

```bash
docker ps
```

You should see a container similar to:

```text
github-engineering-mentor-db
```

### 6. Initialize the Database

Run the initialization script once to create the required SurrealDB tables.

```bash
python mentor/database/init_db.py
```

This creates the following tables if they do not already exist:

- repository
- chunk
- conversation
- memory

This step only needs to be performed once for a new database.

### 7. Apply Django Migrations

```bash
python manage.py migrate
```

This creates Django's relational database tables (authentication, sessions, admin, and other Django models). It is separate from the SurrealDB setup.

### 8. Start the Django Server

```bash
python manage.py runserver
```

The application should now be available at:

```
http://127.0.0.1:8000
```
---

## Running the MCP Server

To expose the application as an MCP server for A2A comuunication, read from [Use the agent using MCP client](<https://github.com/Parisa-Reza/github-brainstorming-agent/tree/main/MCP_client_plugin_guideline>)

---

## Future Improvements

* Support private GitHub repositories
* Better visualization of repository structure
* Streaming responses
* User authentication
* Repository indexing optimization

---

## Author

**Parisa Reza**

GitHub: https://github.com/Parisa-Reza
