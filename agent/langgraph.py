from tools.list_encryption import list_encryption
from tools.decryption import list_decryption
from application_context import init_context, get_context

#Initialise context
application_context = init_context()

l = [4,5,5,6]

el = list_encryption(l)
print(f"the el is {el}")
el += [1,1,1,1]
print(list_decryption(el))

