import nltk
import string

nltk.data.path.append('/home/rithi/nltk_data')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words =  set(stopwords.words('english'))

def clean_text(text: str) -> str:
    text = text.lower() #lowercase
    words = word_tokenize(text) #tokenize the text into words
    words_no_punct = [word for word in words if word not in string.punctuation] # removes puncutation
    words_no_stopwords = [word for word in words_no_punct if word not in stop_words] # removes stopwords
    return " ".join(words_no_stopwords)



