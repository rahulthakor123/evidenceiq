from truth_investigator.retrieval.tfidf_retriever import (
    TfidfRetriever,
)


def test_tfidf_retrieval():

    documents = [
        {
            "document_id": "doc_001",
            "text": "The treatment reduced blood pressure.",
        },
        {
            "document_id": "doc_002",
            "text": "The study investigated diabetes.",
        },
        {
            "document_id": "doc_003",
            "text": "Researchers measured blood pressure.",
        },
    ]

    retriever = TfidfRetriever(documents)

    query = "The treatment reduced blood pressure."

    results = retriever.retrieve(
        "The treatment reduced blood pressure.",
        top_k=2,
    )

    # Print the experiment result
    print("\n" + "=" * 60)
    print("TF-IDF RETRIEVAL EXPERIMENT")
    print("=" * 60)

    print("\nQuery:")
    print(query)

    print("\nRetrieved Documents:")

    for rank, result in enumerate(results, start=1):
        print(f"\nRank {rank}")
        print(f"Document ID : {result.document_id}")
        print(f"Score       : {result.score:.4f}")
        print(f"Text        : {result.text}")

    print("\n" + "=" * 60)

    assert len(results) == 2
    assert results[0].document_id == "doc_001"
    assert results[0].score >= results[1].score