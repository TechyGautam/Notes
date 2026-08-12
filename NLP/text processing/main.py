from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "I love Python Python",
    "I love Machine Learning",
    "Python is powerful"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(sentences)

print(vectorizer.get_feature_names_out())
print(X.toarray())