import tenseal as ts
from application_context import get_context

def list_encryption(l:list)->list:
    context = get_context()
    if context:
        print(type(ts.bfv_vector(context, l)))
        return ts.bfv_vector(context, l)
    else:
        return ValueError("No context found while using the tool list_encryption")
     


