from langchain_core.tools import tool
from utils.context_manager import get_context
from utils.serialise_deserealise import deserialize_bfvvector

@tool
def decrypt_interest_results(file_path: str = "data/interest_results") -> dict:
    """
    Decrypts similarity scores stored in the interest_results file.

    Args:
        file_path (str): Path to the file containing movie similarity scores (default: data/interest_results)

    Returns:
        dict: Dictionary of movie titles and their decrypted similarity scores
    """
    context = get_context()
    results = {}

    with open(file_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        if not line.strip():
            continue
        title, encrypted_b64 = line.strip().split(":")
        encrypted_score = deserialize_bfvvector(encrypted_b64, context)
        decrypted = encrypted_score.decrypt().tolist()
        results[title] = decrypted[0] if isinstance(decrypted, list) else decrypted

    return results
