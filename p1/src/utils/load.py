import pymupdf

from pathlib import Path
from docx import Document

class Loader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _get_file_extension(self):
        return Path(self.file_path).suffix.lower()

    def _load_pdf(self):
        try:
            with pymupdf.open(self.file_path) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()

            return text.replace("\n", " ")
        except Exception as e:
            raise e

    def get_text(self):
        if self._get_file_extension() == ".pdf":
            return self._load_pdf()

        raise ValueError("Unsupported file type")