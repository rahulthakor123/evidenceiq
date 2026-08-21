from datetime import datetime

from truth_investigator.models.document import Document


def test_valid_document():
    document = Document(
        document_id="doc_001",
        title="Test Document",
        text="This is a test document.",
        source_id="source_001",
        file_type="txt",
        created_at=datetime.now(),
    )

    assert document.document_id == "doc_001"
    assert document.text == "This is a test document."