import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import re
import string

# Uncomment this line to download stop words if not already downloaded
#nltk.download('stopwords')
#nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))

def cleanText(texts):
    texts = re.sub(r'http\S+|www\S+|https\S+', '', texts, flags=re.MULTILINE)
    texts = re.sub(r'\d+', '', texts)
    texts = re.sub(r'\s+', ' ', texts).strip()
    texts = texts.translate(str.maketrans('', '', string.punctuation))
    # Tokenize the text
    words = word_tokenize(texts)
    # Remove stop words
    texts = ' '.join(word for word in words if word not in stop_words)
    texts = texts.lower()
    return texts