import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import re

# Uncomment these lines to download stop words if not already downloaded
# nltk.download('stopwords')
# nltk.download('punkt')

stop_words = set(stopwords.words('english'))

def cleanText(texts):
    # Split the text into paragraphs using a single newline
    paragraphs = texts.strip().split('\n\n')
    if len(paragraphs) < 2:
        paragraphs = texts.strip().split('\n')  # Fallback to single newline if needed

    cleaned_paragraphs = []
    
    for paragraph in paragraphs:
        # Remove URLs, numbers, and punctuation
        paragraph = re.sub(r'http\S+|www\S+|https\S+', '', paragraph, flags=re.MULTILINE)
        paragraph = re.sub(r'\d+', '', paragraph)
        paragraph = re.sub(r'[^\w\s]', '', paragraph)  # Remove punctuation
        paragraph = re.sub(r'\s+', ' ', paragraph).strip()
        paragraph = paragraph.lower()
        
        # Tokenize and remove stop words
        tokens = word_tokenize(paragraph)
        tokens = [word for word in tokens if word not in stop_words]
        
        # Join tokens back into a single sentence
        cleaned_paragraph = ' '.join(tokens)
        cleaned_paragraphs.append(cleaned_paragraph)
    
    # Store cleaned paragraphs as para1 and para2
    para1 = cleaned_paragraphs[0] if len(cleaned_paragraphs) > 0 else ''
    para2 = cleaned_paragraphs[1] if len(cleaned_paragraphs) > 1 else ''
    return para1, para2