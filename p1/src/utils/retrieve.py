import chromadb
from chromadb.config import Settings
from p1.src.utils.embed import Embed

class Retrieve:
    def __init__(self, db_path: str, db_name: str):
        self.db_name = db_name
        self.db_path = db_path
        self.client = chromadb.PersistentClient(path=db_path,  settings=Settings(allow_reset=True))

    def _load_database(self):
        if self.db_name not in [collection.name for collection in self.client.list_collections()]:
            raise ValueError(f"Database {self.db_name} do not exist. Please verify database name.")
        try:
            database = self.client.get_collection(name=self.db_name)
        except Exception as e:
            raise ValueError(f"Could not find database named {self.db_name}. {e}")
        
        return database
    
    def get(self, query: str, n_results: int = 5, distance_threshold: float = 0.75):
        # Generate query embedding
        query_embs = Embed(
            model_name="nomic-embed-text:latest",
            input=query
        ).generate()

        # Fetch a larger candidate pool
        results = self._load_database().query(
            query_embeddings=query_embs,
            n_results=50
        )

        # Extract safely
        documents = results.get("documents", [[]])[0]
        distances = results.get("distances", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        if not documents:
            return ["Did not find any relevant documents. Please decline to answer."]

        # Filter + sort by distance (lower is better)
        filtered = sorted(
            [
                (doc, distance, metadata)
                for doc, distance, metadata in zip(documents, distances, metadatas)
                if distance <= distance_threshold
            ],
            key=lambda x: x[1]
        )

        context = [doc for doc, _, _ in filtered[:n_results]]

        if not context:
            return ["Did not find any relevant documents. Please decline to answer."]

        return context
