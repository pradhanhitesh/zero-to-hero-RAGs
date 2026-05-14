import chromadb
from chromadb.config import Settings

class Store:
    def __init__(self, db_name: str, db_path: str):
        # Always reset the existing db
        client = chromadb.PersistentClient(path=db_path, settings=Settings(allow_reset=True))
        client.reset()

        self.collection = client.create_collection(name=db_name)

    def insert(self, ids: list[int], embeddings: list[int], text: list[str], metadatas: list[dict]):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=text,
            metadatas=metadatas
        )
        return self.collection