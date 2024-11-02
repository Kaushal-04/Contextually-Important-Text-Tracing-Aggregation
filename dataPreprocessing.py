import string
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from dataCollection import dataCollect

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

    return para1, para2


para1, para2 = process_text(dataCollect())

# Print the results
print("Paragraph 1 Processed Sentences:")
for sentence in para1:
    print(sentence)

print("\nParagraph 2 Processed Sentences:")
for sentence in para2:
    print(sentence)
