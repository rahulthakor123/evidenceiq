from sklearn.feature_extraction.text import TfidfVectorizer


def create_tfidf(documents: list[str]):

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(documents)

    return vectorizer, matrix