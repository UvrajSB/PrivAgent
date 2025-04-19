import tenseal as ts
from application_context import get_context
from tools.serialise_deserealise import serialize_bfvvector, deserialize_bfvvector
from langchain_core.tools import tool

def list_decryption(el : str)->list:
    """
    Homomorphic Decryption of a base64-encoded BFV-encrypted vector into a list of plaintext integers.

    Args:
        el (str): A base64-encoded string representing a TenSEAL BFVVector.

    Returns:
        list: A list of decrypted integers from the encrypted vector.
    """
    print(f"Called decryption with input: {el}")
    el = deserialize_bfvvector(el)
    return el.decrypt()
