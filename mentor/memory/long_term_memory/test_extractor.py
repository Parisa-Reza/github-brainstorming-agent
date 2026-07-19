from mentor.memory.long_term_memory.memory_extractor import (
    MemoryExtractor,
)

extractor = MemoryExtractor()

memories = extractor.extract(

    "I prefer Python examples.",

    "Okay.",

)

print(memories)