import torch


def cosine_similarity(
    embedding_a: torch.Tensor,
    embedding_b: torch.Tensor,
) -> float:

    similarity = torch.nn.functional.cosine_similarity(
        embedding_a,
        embedding_b,
        dim=0,
    )

    return float(similarity.item())