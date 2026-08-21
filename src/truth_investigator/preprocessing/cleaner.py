import re


def remove_urls(text: str) -> str:
    return re.sub(r"https?://\S+|www\.\S+", "", text)


def remove_html_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def clean_text(text: str) -> str:
    text = remove_urls(text)
    text = remove_html_tags(text)
    text = normalize_whitespace(text)

    return text