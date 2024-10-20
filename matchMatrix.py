import nltk
from nltk import pos_tag, word_tokenize
import numpy as np

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

input_text1 = """The cat is on the mat. Dogs are friendly animals. 
                  The sun is shining bright. Cats enjoy playing outside."""
input_text2 = """A dog is on the mat. Cats are curious creatures. 
                  The weather is lovely today. Dogs love to run in the park."""

# Function to extract sentences and their nouns
def extract_nouns(text):
    sentences = nltk.sent_tokenize(text)
    nouns_per_sentence = []
    
    for sentence in sentences:
        words = word_tokenize(sentence)
        pos_tags = pos_tag(words)
        nouns = [word for word, tag in pos_tags if tag.startswith('NN')]
        nouns_per_sentence.append(nouns)
    
    return sentences, nouns_per_sentence

# Extract nouns from both input texts
sentences1, nouns1 = extract_nouns(input_text1)
sentences2, nouns2 = extract_nouns(input_text2)

# Initialize the match matrix
num_sentences1 = len(sentences1)
num_sentences2 = len(sentences2)
match_matrix = np.zeros((num_sentences1, num_sentences2), dtype=int)

# Populate the match matrix based on common nouns
for i in range(num_sentences1):
    for j in range(num_sentences2):
        common_nouns = set(nouns1[i]) & set(nouns2[j])  # Intersection of nouns
        match_matrix[i][j] = len(common_nouns)  # Count of common nouns

# Print the results
print("Sentences from Input Text 1:")
print(sentences1)
print("Nouns per Sentence from Input Text 1:")
print(nouns1)

print("\nSentences from Input Text 2:")
print(sentences2)
print("Nouns per Sentence from Input Text 2:")
print(nouns2)

print("\nMatch Matrix:")
print(match_matrix)
