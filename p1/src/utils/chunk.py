from langchain_text_splitters import (RecursiveCharacterTextSplitter,
                                      CharacterTextSplitter,
                                      MarkdownHeaderTextSplitter)
from typing import Literal

class Chunk:
    def __init__(self, text: str, chunking_method: Literal["Recursive Character", "Character", "Markdown Header"]):
        self.text = text
        self.chunking_method = chunking_method

    def _recursive_char_splitter(self, chunk_size: int = 100, chunk_overlap: int = 0):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return text_splitter.split_text(self.text)
    
    def _char_splitter(self, chunk_size: int = 100, chunk_overlap: int = 0):
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            encoding_name="cl100k_base", 
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap
        )
        return text_splitter.split_text(self.text)
    
    def _markdown_split(self):
        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
        return markdown_splitter.split_text(self.text)

    def get_chunks(self, chunk_size: int = 100, chunk_overlap: int = 0):
        if self.chunking_method == "Recursive Character":
            return self._recursive_char_splitter(chunk_size, chunk_overlap)
        elif self.chunking_method == "Character":
            return self._char_splitter(chunk_size, chunk_overlap)
        elif self.chunking_method == "Markdown Header":
            return self._markdown_split()
