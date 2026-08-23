from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "The cat sat on the mat.",
    "The dog sat on the mat.",
    "The cat likes food.",
]

def create_bow(documents: list[str]):
    vectorizer = CountVectorizer()

    matrix = vectorizer.fit_transform(documents)

    return vectorizer, matrix