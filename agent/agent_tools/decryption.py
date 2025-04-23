import tenseal as ts
from utils.context_manager import get_context
from utils.serialise_deserealise import serialize_bfvvector, deserialize_bfvvector
from langchain_core.tools import tool

def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()
    
    
@tool
def list_decryption(file_path : str)->list:
    """
    Homomorphic Decryption of a base64-encoded BFV-encrypted vector into a list of plaintext integers.

    Args:
        file_path (str): path of the file where base64-encoded BFV-encrypted vector is stored.

    Returns:
        list: A list of decrypted integers from the encrypted vector.
    """
    context = get_context()
    el = read_file(file_path)
    el = deserialize_bfvvector(el, context)
    return el.decrypt().tolist()
