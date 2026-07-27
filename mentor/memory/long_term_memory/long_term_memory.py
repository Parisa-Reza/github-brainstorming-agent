from mentor.memory.long_term_memory.memory_store import (
    MemoryStore,
)
from mentor.memory.long_term_memory.memory_extractor import (
    MemoryExtractor,
)

class LongTermMemory:

    def __init__(self):

        self.store = MemoryStore()
        self.extractor = MemoryExtractor()


    def process(

        self,

        conversation_id,

        user_message,

        assistant_message,

    ):

        memories = self.extractor.extract(

            user_message,

            assistant_message,

        )

        for memory in memories:

            self.save(

                conversation_id,

                memory,

            )
    def save(
        self,
        conversation_id,
        fact,
    ):

        self.store.save_memory(
            conversation_id,
            fact,
        )

    def get(
        self,
        conversation_id,
    ):

        memories = self.store.get_memories(
            conversation_id,
        )

        return [
            memory["fact"]
            for memory in memories
        ]

    def clear(
        self,
        conversation_id,
    ):

        self.store.delete_memories(
            conversation_id,
        )