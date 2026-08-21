from truth_investigator.ingestion.text_loader import load_text_file


def test_load_text_file():
    text = load_text_file("data/raw/sample.txt")

    assert "Earth" in text