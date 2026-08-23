from truth_investigator.extraction.sentence_segmenter import (
    segment_sentences,
)


def test_segment_sentences():
    text = (
        "Researchers conducted a study. "
        "The treatment reduced blood pressure. "
        "The results were significant."
    )

    sentences = segment_sentences(text)

    assert len(sentences) == 3
    assert sentences[0] == "Researchers conducted a study."