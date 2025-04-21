import tenseal as ts
import os 

_context = None

def init_context():
    global _context
    context_file = "utils/context.tenseal"

    if not os.path.exists(context_file):
        _context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)
        _context.generate_galois_keys()
        _context.generate_relin_keys()
        _context.global_scale = 2**40 
        print("Context Initialised")
        with open(context_file, "wb") as f:
            f.write(_context.serialize(save_public_key=True,
                                    save_secret_key=True,
                                    save_galois_keys=True,
                                    save_relin_keys=True))
        print("Context saved in file")
    else:
        print("Context file already exists, skipping initialization.")

def get_context():
    with open("utils/context.tenseal", "rb") as f:
        _context = ts.context_from(f.read())
    return _context
