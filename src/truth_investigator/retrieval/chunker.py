def chunk_text(
    text: str,
    sentences_per_chunk: int = 3,
) -> list[str]:

    sentences = [
        sentence.strip()
        for sentence in text.split(".")
        if sentence.strip()
    ]

    chunks = []

    for i in range(
        0,
        len(sentences),
        sentences_per_chunk,
    ):

        chunk = ". ".join(
            sentences[
                i:i + sentences_per_chunk
            ]
        )

        if chunk:
            chunks.append(chunk + ".")

    return chunks