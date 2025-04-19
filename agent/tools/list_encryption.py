import tenseal as ts
from application_context import get_context
from tools.serialise_deserealise import serialize_bfvvector, deserialize_bfvvector

def list_encryption(l:list)-> str:
    """
    Homomorphic Encryption of a list of numbers.

    Args:
        l (list): A list of integers to be encrypted.

    Returns:
        str: A base64-encoded string representing the encrypted TenSEAL BFVVector.
    """
    context = get_context()
    if context:
        print(f"Called encryption with input: {l}")
        return serialize_bfvvector(ts.bfv_vector(context, l))
    else:
        return ValueError("No context found while using the tool list_encryption")
     


