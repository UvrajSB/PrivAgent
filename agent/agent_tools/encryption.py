import tenseal as ts
from utils.context_manager import get_context, init_context
from utils.serialise_deserealise import serialize_bfvvector, deserialize_bfvvector
from langchain_core.tools import tool
import os


@tool
def list_encryption(l:list)-> str:
    """
    Doing Homomorphic Encryption of a list of numbers.

    Args:
        l (list): A list of integers to be encrypted.

    Returns:
        str: path to the file where encrypted object is stored
    """
    context = get_context()
    if context:
        print(f"Called encryption with input: {l}")
        file_path = "data/encrypted_data.txt"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(serialize_bfvvector(ts.bfv_tensor(context, l)))
        return file_path
    else:
        return ValueError("No context found while using the tool list_encryption")
