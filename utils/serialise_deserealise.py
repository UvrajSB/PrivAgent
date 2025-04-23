import base64
import tenseal as ts

def serialize_bfvvector(bfv_vector: ts.BFVVector) -> str:
    serialized_bytes = bfv_vector.serialize()
    encoded_string = base64.b64encode(serialized_bytes).decode("utf-8")
    return encoded_string


def deserialize_bfvvector(encoded_string: str, context: ts.Context) -> ts.BFVVector:
    serialized_bytes = base64.b64decode(encoded_string.encode("utf-8"))
    return ts.bfv_tensor_from(context, serialized_bytes)
