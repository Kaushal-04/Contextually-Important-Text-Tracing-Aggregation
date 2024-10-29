import re
from dataCollection import dataCollect  # Import the function

# Fetch the text from dataCollection.py
texts = dataCollect()

# Use the defined text directly
paragraphs = texts.strip().split('\n\n')

# Extract sentences from paragraphs
sentences = []
for paragraph in paragraphs:
    sentences.extend(re.split(r'(?<=[.!?]) +', paragraph))

# Extract words from sentences
words = []
for sentence in sentences:
    words.extend(re.findall(r'\b\w+\b', sentence))

# Join the words into a single string
joined_words = ' '.join(words)

# Print the result
print("Joined Words:")
print(joined_words)
