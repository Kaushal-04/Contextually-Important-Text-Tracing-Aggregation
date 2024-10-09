from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def vectorize_text(text):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    return pd.DataFrame(X.toarray(), columns=feature_names)
