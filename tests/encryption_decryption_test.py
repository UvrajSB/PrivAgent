import tenseal as ts
from utils.serialise_deserealise import serialize_bfvvector, deserialize_bfvvector
from utils.context_manager import init_context, get_context

def test_encrypt_decrypt():
    init_context()
    context = get_context()
    data = [1, 2, 3, 4]
    encoded_string = serialize_bfvvector(ts.bfv_vector(context, data))
    result = deserialize_bfvvector(encoded_string, context)
    print(result)
    result = result.decrypt()
    print(result)
    assert result == data
    
def test_encrypt_decrypt_file():
    init_context()
    context = get_context()
    data = [1, 2, 3, 4]
    encoded_string = serialize_bfvvector(ts.bfv_vector(context, data))
    
    with open("temp.txt", "w") as f:
        f.write(encoded_string)
        
    encoded_string = None
    with open("temp.txt", "r") as f:
        encoded_string = f.read()
    result = deserialize_bfvvector(encoded_string, context)
    print(result)
    result = result.decrypt()
    print(result)
    assert result == data
    
def test_stored_encrypted_data():
    init_context()
    context = get_context()
    encoded_string = None
    with open("agent/encrypted_data/encrypted_vector.txt", "r") as f:
        encoded_string = f.read()
        
    result = deserialize_bfvvector(encoded_string, context)
    print(result)
    result = result.decrypt()
    print(result)
        

if __name__ == "__main__":
    test_encrypt_decrypt()
    test_encrypt_decrypt_file()
    test_stored_encrypted_data()