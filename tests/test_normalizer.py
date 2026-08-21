from truth_investigator.preprocessing.normalizer import normalize_text


def test_normalize_text():
    text = "  HELLO WORLD  "

    result = normalize_text(text)

    assert result == "hello world"