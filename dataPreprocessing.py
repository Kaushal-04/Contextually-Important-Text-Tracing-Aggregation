import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import re
from dataCollection import dataCollect

# Uncomment this line to download stop words if not already downloaded
# nltk.download('stopwords')
# nltk.download('punkt')

stop_words = set(stopwords.words('english'))

def cleanText(texts):
    # Remove URLs, numbers, and punctuation
    texts = re.sub(r'http\S+|www\S+|https\S+', '', texts, flags=re.MULTILINE)
    texts = re.sub(r'\d+', '', texts)
    texts = re.sub(r'[^\w\s]', '', texts)  # Remove punctuation
    texts = re.sub(r'\s+', ' ', texts).strip()
    texts = texts.lower()
    
    # Tokenize and remove stop words
    tokens = word_tokenize(texts)
    tokens = [word for word in tokens if word not in stop_words]
    
    # Join tokens back into a single sentence
    cleaned_sentence = ' '.join(tokens)
    return cleaned_sentence