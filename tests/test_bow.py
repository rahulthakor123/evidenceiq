from truth_investigator.representation.bow import create_bow


def test_create_bow():

    documents = [
        "the cat eats food",
        "the dog eats food",
    ]

    vectorizer, matrix = create_bow(documents)

    vocabulary = vectorizer.get_feature_names_out()

    print("Vocabulary:")
    print(vocabulary)

    print("Matrix:")
    print(matrix.toarray())

    assert len(vocabulary) > 0
    assert matrix.shape[0] == 2