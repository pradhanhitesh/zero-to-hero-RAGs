import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from rank_bm25 import BM25Okapi

# Download necessary NLTK datasets
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def clean_text(text):
    # 1. Lowercase the text
    text = text.lower()
    
    # 2. Remove URLs and HTML tags
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'<.*?>', '', text)
    
    # 3. Remove punctuation and numbers
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    
    # 4. Tokenization (Break into words)
    tokens = word_tokenize(text)
    
    # 5. Stop Word Removal
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [word for word in tokens if word not in stop_words]
    
    return " ".join(cleaned_tokens)

def bm25(corpus: list[str], query: str, n_results: int = 25):
    tokenized_corpus = [doc.split(" ") for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    tokenized_query = query.split(" ")
    top_doc = bm25.get_top_n(tokenized_query, corpus, n=n_results)

    return top_doc