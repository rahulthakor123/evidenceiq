import torch

from truth_investigator.representation.similarity import (
    cosine_similarity,
)


def test_cosine_similarity():

    a = torch.tensor([1.0, 0.0])
    b = torch.tensor([1.0, 0.0])

    score = cosine_similarity(a, b)

    assert score > 0.99