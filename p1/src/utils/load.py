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

    def _load_docx(self):
        try:
            doc = Document(self.file_path)
            text = ""
            for para in doc.paragraphs:
                text += para.text
            
            return text.replace("\n", " ")
        except Exception as e:
            raise e

    def _load_md(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return text
        except Exception as e:
            raise e

    def get_text(self):
        if self._get_file_extension() == ".pdf":
            return self._load_pdf()
        elif self._get_file_extension() == ".docx":
            return self._load_docx()
        elif self._get_file_extension() == ".md":
            return self._load_md()

        raise ValueError("Unsupported file type")