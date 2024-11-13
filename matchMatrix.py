from dataPreprocessing import para1 , para2
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required NLTK resources
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

def get_nouns(sentence):
    """Extract nouns from a given sentence."""
    words = word_tokenize(sentence)
    pos_tags = pos_tag(words)
    
    # Return a set of unique nouns
    nouns = {word for word, tag in pos_tags if tag in ('NN', 'NNS', 'NNP', 'NNPS')}
    return nouns

def create_match_matrix(para1, para2):
    """Create a match matrix comparing nouns in sentences of two paragraphs."""
    size = min(len(para1), len(para2))  # Use the smaller size of the two
    match_matrix = [[0] * size for _ in range(size)]
    
    # Get nouns for each sentence in both paragraphs
    nouns_para1 = [get_nouns(sentence) for sentence in para1]
    nouns_para2 = [get_nouns(sentence) for sentence in para2]
    
    # Fill the match matrix
    for i in range(size):
        for j in range(size):
            # Count common nouns between sentence i of para1 and sentence j of para2
            common_nouns = nouns_para1[i].intersection(nouns_para2[j])
            match_matrix[i][j] = len(common_nouns)

    return match_matrix


match_matrix = create_match_matrix(para1, para2)

# # Print the match matrix
# print("Match Matrix:")
# for row in match_matrix:
#     print(row)
