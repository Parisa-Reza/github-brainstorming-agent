
```text
GitHub Repo URL
      │
      ▼
[1] Clone/Download repo
      │
      ▼
[2] Walk through files ──► Read each one
      │
      ▼
[3] Wrap each file as a "Document" (path + content)
      │
      ▼
[4] Slice each Document's content into "Chunks" (≤1000 chars each)
      ├── chunk_index starts at 0 for EACH document, counts up (0, 1, 2...)
      └── Resets back to 0 when moving to the next document
      │
      ▼
[5] Send each Chunk's text to an embedding model
      │
      ▼
[6] Model returns a fixed-size vector (e.g., 384 numbers) per chunk
      │
      ▼
[7] Store/pair each vector with its (file_path, chunk_index)
      └── Makes each embedding traceable back to "which file" + "which piece"
      │
      ▼
Ready for search / comparison
      └── When a search matches an embedding, use (file_path, chunk_index)
          to find and display the original chunk text

```