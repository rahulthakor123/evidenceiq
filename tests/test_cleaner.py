from truth_investigator.preprocessing.cleaner import clean_text


def test_clean_text():
    text = """
    Hello    world!

    Visit https://example.com

    <p>This is a test.</p>
    """

    result = clean_text(text)

    assert "https://example.com" not in result
    assert "<p>" not in result
    assert result == "Hello world! Visit This is a test."