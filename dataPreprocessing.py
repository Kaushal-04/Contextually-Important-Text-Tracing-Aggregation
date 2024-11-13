import string
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize

# Download required NLTK resources
#nltk.download('punkt')
#nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def process_sentence(sentence):
    # Clean the sentence
    cleaned = clean_text(sentence)
    # Tokenize the cleaned sentence
    tokens = word_tokenize(cleaned)
    # Apply lemmatization (avoid stemming for better word forms)
    lemmatized = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return ' '.join(lemmatized)

def process_text(input_text):
    # Split input into paragraphs
    paragraphs = input_text.strip().split('\n\n')
    para1, para2 = [], []

    for i, paragraph in enumerate(paragraphs):
        # Split each paragraph into sentences
        sentences = sent_tokenize(paragraph)
        for sentence in sentences:
            processed_sentence = process_sentence(sentence)
            if i == 0:
                if processed_sentence:  # Only add non-empty processed sentences
                    para1.append(processed_sentence)
            elif i == 1:
                if processed_sentence:  # Only add non-empty processed sentences
                    para2.append(processed_sentence)

    # Ensure both paragraphs have the same number of sentences
    max_len = max(len(para1), len(para2))
    while len(para1) < max_len:
        para1.append('')  # Add empty string if para1 is shorter
    while len(para2) < max_len:
        para2.append('')  # Add empty string if para2 is shorter

    return para1, para2