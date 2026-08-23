from truth_investigator.ingestion.text_loader import load_text_file
from truth_investigator.preprocessing.cleaner import clean_text
from truth_investigator.preprocessing.normalizer import normalize_text
from truth_investigator.extraction.sentence_segmenter import segment_sentences
from truth_investigator.extraction.claim_extractor import (
    extract_candidate_claims,
)


def process_document(file_path: str):

    # 1. Load
    text = load_text_file(file_path)

    # 2. Clean
    cleaned_text = clean_text(text)

    # 3. Normalize
    normalized_text = normalize_text(cleaned_text)

    # 4. Sentence segmentation
    sentences = segment_sentences(normalized_text)

    # 5. Candidate claim extraction
    source_id = "research_sample"

    claims = extract_candidate_claims(
        sentences,
        source_id,
    )

    return claims


if __name__ == "__main__":

    file_path = "data/raw/research_sample.txt"

    claims = process_document(file_path)

    print("\nCandidate Claims:\n")

    for index, claim in enumerate(claims, start=1):
        print(f"{index}. {claim.text}")