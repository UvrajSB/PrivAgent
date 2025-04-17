import tenseal as ts
from application_context import get_context

def list_decryption(el : ts.tensors.bfvvector.BFVVector)->list:
        return el.decrypt()
