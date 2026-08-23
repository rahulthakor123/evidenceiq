from truth_investigator.representation.pipeline import build_representations


def test_representation_pipeline():

    documents = [
        "The cat sat on the mat.",
        "The dog sat on the mat.",
        "The cat likes food.",
    ]

    result = build_representations(documents)

    print("\nBoW:")
    print(result["bow"]["matrix"].toarray())

    print("\nTF-IDF:")
    print(result["tfidf"]["matrix"].toarray())

    assert result["bow"]["matrix"].shape[0] == 3
    assert result["tfidf"]["matrix"].shape[0] == 3