from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from utils.serialise_deserealise import deserialize_bfvvector, serialize_bfvvector
from utils.context_manager import get_context
import os
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("add-one", port=os.getenv("MCP_SERVER_PORT"), log_level=os.getenv("MCP_SERVER_LOG_LEVEL"))

class EncryptedVector(BaseModel):
    vector_b64: str
    
def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()

@mcp.tool()
def add_one() -> str:
    """
    Performs homomorphic addition of 1 to each element of an encrypted BFV vector.

    This tool:
    - Reads a base64-encoded BFV-encrypted vector from a local file (`data/encrypted_data.txt`).
    - Deserializes the encrypted vector using the active TenSEAL context.
    - Adds 1 to each encrypted element using homomorphic addition.
    - Serializes the updated vector back to a base64 string.
    - Overwrites the original file with the new encrypted vector.

    Returns:
        str: Base64-encoded string of the updated encrypted BFV vector.
    """
    context = get_context()
    file_path = "data/encrypted_data.txt"
    vector_b64 = read_file(file_path)
    encrypted_vector = deserialize_bfvvector(vector_b64, context)
    added_vector = encrypted_vector + 1

    # Serialize and save
    result_b64 = serialize_bfvvector(added_vector)
    with open("data/encrypted_data.txt", "w") as f:
        f.write(result_b64)

    return result_b64


if __name__ == "__main__":
    mcp.run(transport="sse")
