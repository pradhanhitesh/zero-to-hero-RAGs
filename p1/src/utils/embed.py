from collections.abc import Sequence
import ollama


class Embed:
    def __init__(
        self,
        model_name: str,
        input: Sequence[str] | str,
        batch_size: int = 20
    ):
        self.model_name = model_name
        self.input = input
        self.batch_size = batch_size

    def _embed_batch(self, batch: list[str]):
        return ollama.embed(
            model=self.model_name,
            input=batch,
            options={"num_ctx": 8192}
        )["embeddings"]

    def generate(self):
        # Single string
        if isinstance(self.input, str):
            return self._embed_batch([self.input])[0]

        # Sequence of strings
        embeddings = []
        for i in range(0, len(self.input), self.batch_size):
            batch = list(self.input[i:i + self.batch_size])
            embeddings.extend(self._embed_batch(batch))

        return embeddings