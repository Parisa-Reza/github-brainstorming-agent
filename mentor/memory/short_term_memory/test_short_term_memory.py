import uuid

from mentor.memory.short_term_memory.short_term_memory import (
    ShortTermMemory,
)


memory = ShortTermMemory()

conversation_id = str(
    uuid.uuid4()
)

memory.save_user_message(
    conversation_id,
    "Hello",
)

memory.save_assistant_message(
    conversation_id,
    "Hi! How can I help?",
)

history = memory.get_history(
    conversation_id
)

print()

print("Conversation")

print("----------------")

for message in history:

    print(
        message["role"],
        ":",
        message["content"],
    )

memory.clear(
    conversation_id
)

print()

print("Conversation Deleted")