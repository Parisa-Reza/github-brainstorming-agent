# Chat Flow — How a Question Becomes a Formatted Answer

This document explains, step by step, what happens from the moment a user types a question until they see a fully formatted response — and what happens differently if the page is reloaded.

# Chat Flow Diagram

```
┌─────────────────────────────────────────────────────────┐
│ 1. USER TYPES A QUESTION                                │
│                                                         │
│ Example: "How does login work?"                         │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 2. chat.js INTERCEPTS THE FORM SUBMIT                   │
│                                                         │
│ - Stops the browser from doing a normal page reload     │
│ - Reads the question from the input                     │
│ - Shows the user's message immediately                  │
│ - Shows a temporary "Thinking..." agent bubble          │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 3. chat.js SENDS A POST REQUEST TO DJANGO               │
│                                                         │
│ Sends:                                                  │
│ - question                                              │
│ - CSRF security token                                   │
│                                                         │
│ Browser ───────────────► chat/views.py                  │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 4. DJANGO GETS THE ACTIVE REPOSITORY                    │
│                                                         │
│ chat/views.py reads from the session:                   │
│ - active repository URL                                 │
│ - earlier chat messages                                 │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 5. DJANGO ASKS ChatService                              │
│                                                         │
│ ChatService gets repository context using:              │
│ - vector search: relevant code/text chunks              │
│ - graph search: related graph nodes, if graph exists    │
│                                                         │
│ It sends the question + context to the LLM/agent.       │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 6. AGENT RETURNS AN ANSWER AS MARKDOWN TEXT             │
│                                                         │
│ Example returned text:                                  │
│                                                         │
│ ## Login flow                                           │
│                                                         │
│ Call `login(user)` first.                               │
│                                                         │
│ ```python                                               │
│ login(user)                                             │
│ ```                                                     │
│                                                         │
│ At this point it is plain text.                         │
│ It is NOT HTML and is not yet visually formatted.       │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 7. chat/views.py CLEANS THE RESPONSE                    │
│                                                         │
│ `answer.strip()` removes empty space at beginning/end.  │
│                                                         │
│ If the entire answer is wrapped like:                   │
│ ```markdown                                             │
│ ...answer...                                            │
│ ```                                                     │
│                                                         │
│ Django removes only that outer wrapper.                 │
│                                                         │
│ Inner Markdown stays unchanged:                         │
│ - ## headings                                           │
│ - **bold**                                              │
│ - `inline code`                                         │
│ - ``` code blocks ```                                   │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 8. DJANGO SAVES THE RAW MARKDOWN IN THE SESSION         │
│                                                         │
│ Session stores:                                         │
│                                                         │
│ {                                                       │
│   role: "assistant",                                    │
│   content: "## Login flow\n\nCall `login(user)`..."     │
│ }                                                       │
│                                                         │
│ Important: it saves Markdown text, not generated HTML.  │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 9. DJANGO RETURNS JSON TO THE BROWSER                   │
│                                                         │
│ {                                                       │
│   "answer": "## Login flow\n\nCall `login(user)`..."    │
│ }                                                       │
│                                                         │
│ Django ───────────────► chat.js                         │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 10. chat.js FORMATS A NEW RESPONSE                      │
│                                                         │
│ `marked.parse(answer)` changes Markdown text into HTML. │
│                                                         │
│ Markdown:             HTML:                             │
│ ## Login flow     →   <h2>Login flow</h2>               │
│ `login(user)`     →   <code>login(user)</code>          │
│ ```python ... ``` →  <pre><code>...</code></pre>        │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 11. chat.js REPLACES "Thinking..."                      │
│                                                         │
│ - Removes the temporary "Thinking..." content           │
│ - Inserts the generated HTML into the agent bubble      │
│ - Scrolls the chat window to the newest message         │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 12. highlight.js COLORS CODE BLOCKS                     │
│                                                         │
│ It finds HTML like:                                     │
│ <pre><code>login(user)</code></pre>                     │
│                                                         │
│ It adds syntax highlighting styles to the code.         │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ 13. USER SEES THE FORMATTED RESPONSE                    │
│                                                         │
│ - headings look like headings                           │
│ - lists look like lists                                 │
│ - inline code is styled                                 │
│ - code blocks are highlighted                           │
└─────────────────────────────────────────────────────────┘
                 WHAT CHANGES AFTER A PAGE RELOAD?
┌─────────────────────────────────────────────────────────┐
│ Browser reloads the page                                │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ Django reads saved chat messages from the session       │
│                                                         │
│ They are saved as raw Markdown, not HTML.               │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ Django puts the raw Markdown into `.markdown-content`   │
│ elements in chat.html                                   │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ markdown-render.js runs after the page loads            │
│                                                         │
│ - finds all `.markdown-content` messages                │
│ - reads their raw Markdown text                         │
│ - uses `marked.parse()` to make HTML                    │
│ - uses `highlight.js` for code blocks                   │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│ Previously saved agent responses look formatted again   │
└─────────────────────────────────────────────────────────┘

NEW MESSAGE:
Agent → Django → JSON Markdown → chat.js → HTML → UI

PAGE RELOAD:
Session Markdown → Django page → markdown-render.js → HTML → UI
```