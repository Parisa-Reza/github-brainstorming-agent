# MCP Client Plugin Guideline

## Overview

This document explains how to connect an external AI agent (for example, a CrewAI agent) to the **GitHub Engineering Mentor** through its MCP server.

---

# Files Required

You only need the following file from this integration package:

- `mentor_client.py`

Use the provided `mentor_client.py` file exactly as supplied.

The client is responsible for:

- Starting the GitHub Engineering Mentor MCP Server
- Connecting to the MCP Server
- Calling the `ask_repository` tool
- Returning the response back to your agent

No modification to `mentor_client.py` is required.

---

# Prerequisites

Clone the GitHub Engineering Mentor repository.



```bash
git clone https://github.com/Parisa-Reza/github-brainstorming-agent.git
```

---

Move into the project

```bash
cd github-brainstorming-agent
```

---

Create a virtual environment

Linux/macOS

```bash
python -m venv venv
```

Windows

```cmd
python -m venv venv
```

---

Activate the virtual environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```cmd
venv\Scripts\activate
```

---

Install all dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Inside **your own project** (not the GitHub Mentor project), create a `.env` file.

Linux/macOS

```text
MENTOR_PROJECT_PATH=/home/username/github-brainstorming-mentor

MENTOR_PYTHON=/home/username/github-brainstorming-mentor/venv/bin/python
```

Windows

```text
MENTOR_PROJECT_PATH=C:\Projects\github-brainstorming-mentor

MENTOR_PYTHON=C:\Projects\github-brainstorming-mentor\venv\Scripts\python.exe
```

---

# Integration

Copy the provided

```
mentor_client.py
```

into your project.

Import it

```python
from mentor_client import MentorClient
```

Call it

```python
answer = await MentorClient().ask_repository(
    repository_url=repository_url,
    question=question,
)
```

The client will automatically

- Start the GitHub Engineering Mentor MCP Server
- Establish the MCP connection
- Execute the `ask_repository` tool
- Return the response to your agent

---

# Running Your Project

After configuring the `.env` file, simply start your own application.

Example

```bash
python main.py
```

or

```bash
python app.py
```

or

```bash
python manage.py runserver
```

depending on your project.

No need to manually start the GitHub Engineering Mentor server.

`mentor_client.py` will automatically launch it when required.

---

# Notes

- Do **not** modify `mentor_client.py`.
- Every developer only needs to update the `.env` file according to where they cloned the GitHub Engineering Mentor project.
- This integration uses the **MCP stdio transport**.
- The GitHub Engineering Mentor project must remain installed locally because the client starts the MCP server from the local project.