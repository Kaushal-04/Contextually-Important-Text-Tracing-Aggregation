from matchMatrix import match_matrix
from dataPreprocessing import para1, para2
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def generate_pairs(match_matrix, para1, para2):
    """Generate relevant sentence pairs based on the match matrix."""
    pairs = []
    row_count = len(match_matrix)

    for i in range(row_count):
        # Find the maximum in the current row
        max_value = max(match_matrix[i])
        max_indices = [j for j, val in enumerate(match_matrix[i]) if val == max_value]

        if max_value == 0:
            # Case 2: Ignore current row if no matches
            continue
        
        elif len(max_indices) == 1:
            # Case 1: Unique maximum, create a pair
            j = max_indices[0]
            pairs.append((para1[i], para2[j]))

        else:
            # Case 3: Multiple matches, calculate cosine similarity
            text1 = para1[i]
            text2_list = [para2[j] for j in max_indices]
            similarities = calculate_cosine_similarity(text1, text2_list)
            best_match_index = max_indices[np.argmax(similarities)]
            pairs.append((para1[i], para2[best_match_index]))

    return pairs

def calculate_cosine_similarity(text1, text2_list):
    """Calculate cosine similarity between a sentence and a list of sentences."""
    documents = [text1] + text2_list
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    return cosine_similarities


pairs = generate_pairs(match_matrix, para1, para2)
# print("Generated Sentence Pairs:")
# for p1, p2 in pairs:
#     print(f"({p1}) with ({p2})")
