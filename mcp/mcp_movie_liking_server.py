from pydantic import BaseModel
from utils.serialise_deserealise import deserialize_bfvvector, serialize_bfvvector
from utils.context_manager import get_context
import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import tenseal as ts
import numpy as np

load_dotenv()

mcp = FastMCP("match_movies", port=os.getenv("MCP_SERVER_PORT"), log_level=os.getenv("MCP_SERVER_LOG_LEVEL"))
    
def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()

def normalize(v):
    norm = np.linalg.norm(v)
    return [int(x * 1000 / norm) for x in v]  # preserve scale

MOVIES = {
    "Inception": normalize([9, 1, 8]),
    "The Notebook": normalize([1, 9, 2]),
    "Interstellar": normalize([8, 2, 9]),
    "The Godfather": normalize([7, 5, 4])
}

@mcp.tool()
def match_movies() -> str:
    """
    Matches encrypted user interest vector with plaintext movie vectors via dot product.
    Saves encrypted similarity scores to 'data/interest_results'.

    Returns:
        str: name of the file where the results are scored
    """
    context = get_context()
    encrypted_b64 = read_file("data/encrypted_data.txt")
    encrypted_vec = deserialize_bfvvector(encrypted_b64, context)

    results = {}

    for title, movie_vector in MOVIES.items():
        plain_vector = np.array(movie_vector, dtype=np.int64)
        similarity_score = encrypted_vec * plain_vector
        score_b64 = serialize_bfvvector(similarity_score)
        results[title] = score_b64

    # Save results to a file
    with open("data/interest_results", "w") as f:
        for title, score_b64 in results.items():
            f.write(f"{title}:{score_b64}\n")

    return "data/interest_results"

if __name__ == "__main__":
    mcp.run(transport="sse")
