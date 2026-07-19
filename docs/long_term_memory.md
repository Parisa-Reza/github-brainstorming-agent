- User sends a new question.

- The system first loads saved long-term facts for that conversation_id.

- These facts are things likely useful in future chats, such as:
User prefers Python examples
User likes concise explanations
User uses Django

- The system also loads short-term memory and retrieves repository context for the current question.

- The AI receives:
Long-term facts about the user
Recent chat messages
Repository code context
The current question

- The AI generates an answer.

- The system saves the user’s question and the assistant’s answer in short-term memory.

- - Then long-term memory processes that question-and-answer pair.

- - A Gemini model reads the pair and decides whether it contains useful lasting information.

- - It ignores temporary things, greetings, thanks, and one-time questions.

- - If it finds useful facts, it stores each fact as a separate database record with:
conversation_id
fact

- Example stored long-term-memory records:
conversation_id: chat-001
fact: User prefers Python examples.

- conversation_id: chat-001
fact: User is working on Hybrid RAG.

- On future questions in the same conversation, these saved facts are loaded again and used to personalize or better understand the answer.

- Unlike short-term memory, long-term memory is not limited to the last 8 messages. It remains stored until clear(conversation_id) deletes it.