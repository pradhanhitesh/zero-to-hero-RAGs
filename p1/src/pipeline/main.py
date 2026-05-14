from p1.src.utils.load import Loader
from p1.src.utils.chunk import Chunk
from p1.src.utils.embed import Embed
from p1.src.utils.store import Store
from p1.src.utils.retrieve import Retrieve
from p1.src.utils.augment import Augment
from p1.src.utils.generate import Generate

def chat():
    print("RAG Chat Ready. Type 'exit' to quit.\n")

    retriever = Retrieve("p1/backend/assets", "test-db")

    while True:
        try:
            query = input("USER: ").strip()

            if not query:
                continue

            if query.lower() in {"exit", "quit", "q"}:
                print("Goodbye.")
                break

            # Retrieve
            context = retriever.get(
                query=query,
                n_results=10
            )

            # Augment
            augmented = Augment(
                context=context,
                query=query
            ).augment()

            # Generate
            response = Generate(
                augmented_text=augmented
            ).generate()

            print(f"\nLLM:\n{response}\n")

        except KeyboardInterrupt:
            print("\nGoodbye.")
            break

        except Exception as e:
            print(f"\n[ERROR] {e}\n")

if __name__ == "__main__":
    # Load and get text
    text = Loader(file_path='/Users/cbr/Library/CloudStorage/OneDrive-CentreforBrainResearch/CBR/Anemia and Cognition/glv158_CheckForStats.pdf').get_text()

    # Chunks
    chunks = Chunk(text, chunking_method="Recursive Character").get_chunks(chunk_size=250, chunk_overlap=50)

    # Embeddings
    embs = Embed(model_name='nomic-embed-text:latest', input=chunks).generate()

    # Store
    ids = [f"id{x+1}" for x in range(len(chunks))]
    metadatas = [{"chunk_number": f"{x+1}"} for x in range(len(chunks))]
    db = Store("rag-db", "p1/backend/assets").insert(ids=ids, embeddings=embs, text=chunks, metadatas=metadatas)

    # Chat
    chat()