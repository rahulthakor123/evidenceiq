import spacy


nlp = spacy.load("en_core_web_sm")


def segment_sentences(text: str) -> list[str]:
    """
    Split text into individual sentences.
    """

    doc = nlp(text)

    return [
        sentence.text.strip()
        for sentence in doc.sents
        if sentence.text.strip()
    ]