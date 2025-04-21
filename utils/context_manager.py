import tenseal as ts

_context = None

def init_context():
    global _context
    _context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)
    _context.generate_galois_keys("blah")
    _context.generate_relin_keys("blah")
    _context.global_scale = 2**40  # only relevant for CKKS

    with open("context.tenseal", "wb") as f:
        f.write(_context.serialize(save_public_key=True,
                                save_secret_key=True,
                                save_galois_keys=True,
                                save_relin_keys=True))

def get_context():
    with open("context.tenseal", "rb") as f:
        _context = ts.context_from(f.read())
