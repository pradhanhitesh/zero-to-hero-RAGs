# Zero to Hero RAGs

Welcome to **Zero to Hero RAGs**, a progressive journey from a simple "Hello World" RAG script to an enterprise-grade Knowledge Operating System. This repository tracks the evolution of Retrieval-Augmented Generation (RAG) systems, building complexity layer by layer.

## Project Roadmap & Tracker

| Project | Name | Status | Difficulty | Key Tech |
| :--- | :--- | :--- | :--- | :--- |
| **p1** | [Local PDF Q&A (rag-pdf-chat)](./p1) | ✅ | Beginner | Python, Ollama, ChromaDB |
| **p2** | Multi-format Knowledge Assistant | ⏳ | Beginner | Unstructured, Docx, Markdown |
| **p3** | Hybrid Search RAG | ⏳ | Intermediate | BM25, Hybrid Ranking |
| **p4** | Conversational Memory RAG | ⏳ | Intermediate | Redis, Chat History |
| **p5** | Citation Research Assistant | ⏳ | Intermediate | Source Attribution, Provenance |
| **p6** | Production API RAG | ⏳ | Advanced | FastAPI, Celery, Workers |
| **p7** | Multi-tenant Enterprise RAG | ⏳ | Advanced | RBAC, Tenant Isolation |
| **p8** | Agentic RAG Assistant | ⏳ | Expert | LangGraph, Tool Calling |
| **p9** | Multimodal RAG | ⏳ | Expert | Vision, Table Extraction |
| **p10** | Knowledge OS | ⏳ | Expert | Observability, Infra Resilience |

## The Progressive Learning Path

### 01. Local PDF Q&A (`rag-pdf-chat`)
The "MNIST of RAG." This project builds the foundational pipeline: document loading, chunking, embeddings, and vector similarity search.
*   **Improvement:** N/A (Foundational layer).

### 02. Multi-format Knowledge Assistant (`rag-knowledge-assistant`)
Extends the system to handle `.docx`, `.md`, and unstructured web data.
*   **Improvement:** It improves on p1 by moving beyond static PDFs to handle diverse real-world ingestion pipelines and metadata extraction.

### 03. Hybrid Search RAG (`hybrid-rag-search`)
Combines semantic (dense) search with keyword (sparse) BM25 retrieval.
*   **Improvement:** It enhances p2 by significantly improving retrieval accuracy for both context-rich queries and exact keyword matches.

### 04. Conversational Memory RAG (`chat-rag-memory`)
Introduces session-aware chat history and memory persistence using Redis.
*   **Improvement:** It evolves from p3 by allowing the assistant to "remember" previous turns, turning single-shot Q&A into a coherent conversation.

### 05. Citation Research Assistant (`research-rag`)
Focuses on source attribution, confidence scoring, and groundedness.
*   **Improvement:** It improves on p4 by providing verifiable citations for every answer, making it suitable for professional research and high-stakes tasks.

### 06. Production API RAG (`rag-api-platform`)
Transitions the project from a CLI script to a full-scale API with FastAPI and background workers.
*   **Improvement:** It moves the local prototype into a scalable architecture with background ingestion, retries, and asynchronous processing.

### 07. Multi-tenant Enterprise RAG (`enterprise-rag`)
Implements Role-Based Access Control (RBAC) and data isolation for multiple users.
*   **Improvement:** It improves on p6 by adding security layers essential for enterprise use, ensuring users can only access their own data silos.

### 08. Agentic RAG Assistant (`agentic-rag-assistant`)
Builds tool-calling agents that can decide when to search the web, run code, or retrieve documents.
*   **Improvement:** It moves beyond passive retrieval to active decision-making, allowing the system to solve complex, multi-step reasoning tasks.

### 09. Multimodal RAG (`multimodal-rag`)
Incorporates Vision-LLMs to interpret images, charts, and complex layouts within documents.
*   **Improvement:** It improves on p8 by enabling the system to "see" and extract meaning from visual data alongside text, handling tables and graphs effectively.

### 10. Knowledge OS (`knowledge-os`)
The ultimate enterprise system with observability (OpenTelemetry), caching, and multi-model fallbacks.
*   **Improvement:** This is the peak evolution, incorporating industrial-grade monitoring, infra resilience, and cost optimization for a true production environment.

## Skills & Engineering Value Learned

This repository isn't just about AI; it's about building **robust engineering systems**:

- **Data Engineering:** Ingestion pipelines, layouts parsing, and MIME detection.
- **Search & Retrieval:** BM25, HNSW, cosine similarity, and hybrid ranking algorithms.
- **Backend Architecture:** Async processing, Celery workers, and API design.
- **DevOps:** Dockerization, environment management, and observability.
- **AI Logic:** Prompt engineering, agentic routing, and multimodal reasoning.

## Getting Started

Each project is self-contained within its own directory. To explore a project:

1.  Navigate to the project folder (e.g., `cd p1`).
2.  Follow the specific `README.md` inside that directory for installation and usage.

---

*“Building the future of knowledge retrieval, one layer at a time.”*
