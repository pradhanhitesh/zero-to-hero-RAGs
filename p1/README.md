# rag-pdf-chat: Local PDF Q&A (Hello World RAG)

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-brightgreen)](https://github.com/yourusername/zero-to-hero-RAGs)
[![Tech Stack: Python](https://img.shields.io/badge/Stack-Python%20%7C%20LangChain%20%7C%20Ollama-blue)](https://www.python.org/)

**rag-pdf-chat** is a foundational RAG (Retrieval-Augmented Generation) implementation designed to provide a "Hello World" experience for building local document-based AI assistants. Upload a PDF (research paper, manual, or report), ask questions, and receive grounded, context-aware answers.

## Overview

This project serves as the "MNIST of RAG," demonstrating the complete lifecycle of a Retrieval-Augmented Generation pipeline. It transitions from raw PDF data to an interactive chat interface where answers are strictly grounded in the provided document.

### Key Features
- **PDF Processing:** Seamlessly load and extract text from complex PDF documents.
- **Intelligent Chunking:** Implements Recursive Character Text Splitting for optimized context retrieval.
- **Vector Embeddings:** Generates high-dimensional embeddings using `nomic-embed-text` via Ollama.
- **Local LLMs:** Support for local LLMs via Ollama for generation.
- **Semantic Search:** Fast and accurate context retrieval from a Chroma vector store.

## Technical Stack

- **Orchestration:** [LangChain](https://www.langchain.com/)
- **Embeddings:** `nomic-embed-text` (Ollama)
- **Vector DB:** [ChromaDB](https://www.trychroma.com/)
- **LLM:** Local `ollama` models (e.g., Llama 3.1)
- **Environment:** Python 3.x

## Core RAG Pipeline

The project implements the following architectural steps:

1.  **Document Loading:** Extracting text from `.pdf` files.
2.  **Chunking:** Breaking long text into smaller, manageable pieces (chunks).
3.  **Embeddings:** Converting text chunks into mathematical vectors.
4.  **Vector Search:** Storing vectors and retrieving relevant chunks based on user queries.
5.  **Prompt Augmentation:** Feeding retrieved context along with the user query into the LLM.
6.  **LLM Generation:** Producing a final answer based on the augmented prompt.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/zero-to-hero-RAGs.git
   cd zero-to-hero-RAGs/p1
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the full RAG pipeline (Load -> Chunk -> Embed -> Store -> Chat) via terminal:

```bash
python -m p1.src.pipeline.main
```

## Concepts Learned
- High-level understanding of **Vector Databases**.
- Practical implementation of **Semantic Search** vs Keyword Search.
- The importance of **Chunking Strategies** in RAG performance.
- Designing **System Prompts** for grounded AI responses.

## Engineering Complexity
- **Complexity:** Low
- **Real-world Relevance:** Moderate (The foundation for any document-based AI tool).
