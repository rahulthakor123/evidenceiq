from truth_investigator.retrieval.chunker import chunk_text


def test_chunk_text():

    text = (
        "The treatment was tested. "
        "The patients were monitored. "
        "Blood pressure decreased. "
        "The researchers continued observation."
    )

    chunks = chunk_text(
        text,
        sentences_per_chunk=2,
    )

    assert len(chunks) == 2
    assert "treatment" in chunks[0]
    assert "researchers" in chunks[1]