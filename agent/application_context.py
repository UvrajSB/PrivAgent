import tenseal as ts

# Global context variable
_context = None

def init_context():
    global _context
    _context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)
    _context.generate_galois_keys()
    _context.generate_relin_keys()
    _context.global_scale = 2**40  # only relevant for CKKS
    return _context

def get_context():
    if _context is None:
        raise ValueError("Context is not initialized. Call init_context() first.")
    return _context
