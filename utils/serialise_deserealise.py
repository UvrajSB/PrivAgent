import base64
import tenseal as ts

def serialize_bfvvector(bfv_vector: ts.BFVVector) -> str:
    serialized_bytes = bfv_vector.serialize()
    encoded_string = base64.b64encode(serialized_bytes).decode("utf-8")
    return encoded_string


def deserialize_bfvvector(encoded_string: str, context: ts.Context) -> ts.BFVVector:
    serialized_bytes = base64.b64decode(encoded_string.encode("utf-8"))
    return ts.bfv_vector_from(context, serialized_bytes)

# import tenseal as ts

# # Global context variable
# _context = None

# def init_context():
#     global _context
#     _context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)
#     _context.generate_galois_keys()
#     _context.generate_relin_keys()
#     _context.global_scale = 2**40  # only relevant for CKKS
#     return _context

# def get_context():
#     if _context is None:
#         raise ValueError("Context is not initialized. Call init_context() first.")
#     return _context

# def test_encrypt_decrypt():
#     init_context()
#     context = get_context()
#     data = [1, 2, 3, 4]
#     encoded_string = serialize_bfvvector(ts.bfv_vector(context, data))
#     result = deserialize_bfvvector(encoded_string, context)
#     print(result)
#     result = result.decrypt()
#     print(result)
#     assert result == data
    
# def test_encrypt_decrypt_file():
#     init_context()
#     context = get_context()
#     data = [1, 2, 3, 4]
#     encoded_string = serialize_bfvvector(ts.bfv_vector(context, data))
    
#     with open("temp.txt", "w") as f:
#         f.write(encoded_string)
        
#     encoded_string = None
#     with open("temp.txt", "r") as f:
#         encoded_string = f.read()
#     result = deserialize_bfvvector(encoded_string, context)
#     print(result)
#     result = result.decrypt()
#     print(result)
#     assert result == data
    
# def test_stored_encrypted_data():
#     init_context()
#     context = get_context()
#     encoded_string = None
#     with open("agent/encrypted_data/encrypted_vector.txt", "r") as f:
#         encoded_string = f.read()
        
#     result = deserialize_bfvvector(encoded_string, context)
#     print(result)
#     result = result.decrypt()
#     print(result)
        
    

# if __name__ == "__main__":
#     test_encrypt_decrypt()
#     test_encrypt_decrypt_file()
#     test_stored_encrypted_data()
