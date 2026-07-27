User sends a new question, for example:
“Why does it save messages this way?”

System loads the last 8 messages from short-term memory.
This helps understand what “it” refers to.

System searches the repository using the current question:
“Why does it save messages this way?”

The repository retriever finds code that looks relevant to that question, such as message-saving functions.

The system puts everything together:
Old chat messages: to understand the conversation
Retrieved repository code: to know the real implementation
New question: what the user wants answered now

The AI generates its answer.

Finally, it saves the new question and its answer for the next turn.

So, in order:

``` text
New question arrives
      ↓
Load recent chat history
      ↓
Search repository using new question
      ↓
Give history + repository code + new question to AI
      ↓
Generate answer
      ↓
Save this question and answer
```

If the new user message is completely unrelated, short-term memory is still loaded because the current code always loads the last 8 messages.

But the AI should simply ignore that history when it is not relevant.

Example:

Earlier chat: questions about message storage
New question: “What does the repository’s README say about installation?”

Flow:
- The system loads the previous 8 messages.
- It searches the repository using the new installation question.
- The AI sees that the old storage discussion is unrelated.
- It answers from the retrieved README/repository context, not from memory.

So short-term memory is always available, but it is only useful for follow-up questions. The repository context is still chosen from the current user question.



The short-term-memory database record stores these fields:
id
Database-generated ID for the conversation record.

session_id
The conversation ID passed by the app. It identifies which chat the messages belong to.

messages
A list containing every saved chat message.

Inside each item in messages, there are two fields:
role
Either "user" or "assistant".

content
The actual message text.

So one database record is like:
```text
id: conversation:abc123
session_id: chat-001
messages: [
  {
    role: user,
    content: "What is short-term memory?"
  },
  {
    role: assistant,
    content: "It stores recent chat messages."
  }
]
```
The application creates session_id and messages. The database provides id.