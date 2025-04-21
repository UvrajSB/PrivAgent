from utils.context_manager import init_context, get_context
import os

def create_context_file():
    init_context()
    file_path = "utils/context.tenseal"
    if os.path.exists(file_path):
        print("File exists")
    else:
        print("File does not exist")

def get_context_from_file():
    context = None
    context = get_context()
    if context:
        print(f"Context read, {context}")
    else:
        print("No context found")
        
    

if __name__ == "__main__":
    create_context_file()
    get_context_from_file()