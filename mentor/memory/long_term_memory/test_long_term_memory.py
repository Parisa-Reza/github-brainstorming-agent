import uuid

from mentor.memory.long_term_memory.long_term_memory import (
    LongTermMemory,
)


memory = LongTermMemory()

conversation_id = str(
    uuid.uuid4()
)

memory.save(
    conversation_id,
    "User prefers Python examples.",
)

memory.save(
    conversation_id,
    "User likes Django.",
)

facts = memory.get(
    conversation_id,
)

print()

print("Long Term Memory")

print("--------------------")

for fact in facts:

    print(fact)

memory.clear(
    conversation_id,
)

print()

print("Memory Deleted")