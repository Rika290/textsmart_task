import nltk
from collections import Counter

nltk.data.path.append('/home/rithi/nltk_data')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

stop_words = set(stopwords.words('english'))

def summarize_text(text: str, top_n: int = 3) -> list:
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    
    # Remove stopwords and punctuation
    words = [w for w in words if w not in stop_words and w not in string.punctuation]
    
    # Word frequency
    freq = Counter(words)
    
    # Score sentences
    sentence_scores = {}
    for sent in sentences:
        word_count = word_tokenize(sent.lower())
        score = sum(freq.get(w, 0) for w in word_count)
        sentence_scores[sent] = score
    
    # Top N sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:top_n]
    return top_sentences

