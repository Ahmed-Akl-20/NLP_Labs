# =========================
# 1. IMPORTS
# =========================
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import NMF, PCA
from sklearn.manifold import TSNE
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier

import numpy as np
# import spacy


# =========================
# 2. TOKENIZATION
# =========================
text = ("Natural Language Processing (NLP) is a subfield of computer science, "
        "artificial intelligence, and computational linguistics concerned with "
        "the interactions between computers and human (natural) languages. "
        "It focuses on how to program computers to process and analyze large "
        "amounts of natural language data.")

tokens = word_tokenize(text)
print("Number of tokens:", len(tokens))
print("First 20 tokens:", tokens[:20])


# =========================
# 3. COUNT VECTORIZER
# =========================
count_vec = CountVectorizer()
X_count = count_vec.fit_transform([text])

print("\nCountVectorizer:")
print(count_vec.get_feature_names_out()[:10])
print(X_count.toarray()[0][:10])


# =========================
# 4. TF-IDF EXAMPLE
# =========================
d0 = 'Geeks for geeks'
d1 = 'Geeks'
d2 = 'r2j'

corpus = [d0, d1, d2]

tfidf = TfidfVectorizer()
result = tfidf.fit_transform(corpus)

print('\nIDF values:')
for word, val in zip(tfidf.get_feature_names_out(), tfidf.idf_):
    print(word, ":", val)

print('\nWord indexes:')
print(tfidf.vocabulary_)

print('\nTF-IDF value:')
print(result)

print('\nTF-IDF values in matrix form:')
print(result.toarray())


# =========================
# 5. TEXT CLASSIFICATION
# =========================
texts = [
    "This movie is amazing!",
    "I hated the plot.",
    "The acting was great.",
    "Waste of time."
]

labels = ["positive", "negative", "positive", "negative"]

# Feature extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25)

# Model
clf = MultinomialNB()
# clf = RandomForestClassifier(n_estimators=100, random_state=42)

clf.fit(X_train, y_train)

# Prediction
prediction = clf.predict(vectorizer.transform(["great"]))
print("\nPrediction for 'great':", prediction)