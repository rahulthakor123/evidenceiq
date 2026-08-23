from truth_investigator.representation.bow import create_bow
from truth_investigator.representation.tfidf import create_tfidf


def build_representations(documents: list[str]):

    bow_vectorizer, bow_matrix = create_bow(documents)

    tfidf_vectorizer, tfidf_matrix = create_tfidf(documents)

    return {
        "bow": {
            "vectorizer": bow_vectorizer,
            "matrix": bow_matrix,
        },
        "tfidf": {
            "vectorizer": tfidf_vectorizer,
            "matrix": tfidf_matrix,
        },
    }