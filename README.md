# Compressy

A Python-based **LZ77 Lossless Compression** application that allows users to compress and decompress text files using the LZ77 algorithm.

## Overview

**Compressy** is a command-line application built to demonstrate the practical implementation of the **LZ77 lossless compression algorithm**.

The application can:

* Compress `.txt` files.
* Decompress compressed files.
* Store compressed data in a text file.
* Reconstruct the original file without losing any data.
* Find repeated patterns using a sliding window.

## How LZ77 Works

LZ77 takes advantage of repeated sequences in the input data.

Instead of storing a sequence that has already appeared, the algorithm stores a reference to its previous occurrence.

Each compressed sequence is represented as:

```text
(offset, length, next_symbol)
```

Where:

* **Offset** — how far back the matching sequence starts.
* **Length** — number of characters in the matching sequence.
* **Next Symbol** — the character immediately after the matched sequence.

If no previous match is found, the application stores:

```text
(0, 0, character)
```

## Sliding Window

The implementation uses a search window with a size of:

```python
WINDOW_SIZE = 10
```

For every position in the input, the algorithm searches the previous 10 characters for the longest possible match.

```text
Search Window          Current Position
───────────────────┬────────────────────
Previous 10 chars  │   Data to process
───────────────────┴────────────────────
                    ↑
                  Current
                  position
```

The window moves forward as the algorithm processes the input.

## Compression

During compression, the application:

1. Reads the input `.txt` file.
2. Searches the previous 10 characters.
3. Finds the longest matching sequence.
4. Creates an LZ77 tag.
5. Moves forward in the input.
6. Writes the generated tags to a new file.

For example, repeated sequences such as:

```text
ABABABAB
```

can be represented using references to previously processed characters instead of storing the same sequence repeatedly.

## Decompression

The decompression process reconstructs the original message from the generated LZ77 tags.

For each tag:

* `(0, 0, character)` means the character is added directly.
* Otherwise, the decoder uses the **offset** and **length** to copy characters from the already reconstructed message.
* The `next_symbol` is then added.

Because LZ77 is a **lossless compression algorithm**, the decompressed data is identical to the original data.

```text
Original File
     |
     v
Compression
     |
     v
LZ77 Tags
     |
     v
Decompression
     |
     v
Original File
```

## Application

Compressy provides a simple command-line interface:

```text
=========================
======== Welcome ========
===== Compressy App =====
=========================

----------------------
|        MENU        |
----------------------
[1]. Compression
[2]. Decompression
[0]. Exit
----------------------
```

### Compression

Select:

```text
[1]. Compression
```

Enter the name of the `.txt` file you want to compress, then provide a name for the generated compressed file.

### Decompression

Select:

```text
[2]. Decompression
```

Enter the name of the compressed file, then provide a name for the reconstructed `.txt` file.

## File Format

The compressed output contains LZ77 tags such as:

```text
[0, 0, 'A']
[0, 0, 'B']
[2, 4, '']
```

The decompression function reads these tags and reconstructs the original message.

## Complexity

Let `N` be the input size.

Since the search window has a fixed size of `10`, the number of positions checked for each character is bounded by a constant.

Therefore, with a fixed window and bounded match length:

```text
Compression:    O(N)
Decompression:  O(N)
Space:          O(N)
```

## Technologies

* Python
* LZ77
* Lossless Data Compression
* File Handling
* Command-Line Interface

## Getting Started

Clone the repository:

```bash
git clone https://github.com/bmohamed-it/compression-by-lz77-python.git
```

Navigate to the project directory:

```bash
cd compression-by-lz77-python
```

Run the application:

```bash
python main.py
```

## Project Structure

```text
compression-by-lz77-python/
│
├── main.py
├── README.md
└── *.txt
```

## Project Goals

This project was developed to gain practical experience with:

* Data compression algorithms
* LZ77
* Sliding-window techniques
* Pattern matching
* File input/output
* Algorithm complexity analysis
* Python programming

## Author

**Bilal Mohamed Abd Al-Hamed**
**Mohamed Tarek Mohamed Hossny**
**Hassan Sameh Hassan**

## License

This project is intended for educational purposes and for learning the fundamentals of lossless data compression.
