from langchain_core.tools import tool

@tool
def add(a: int, b:int)->int:
    """
    Adds two integers a and b and returns the result of addition which is an int as well.
    
    Args:
    a (int) : first integer
    b (int) : second integer
    
    Returns:
    int : sum of a and b
    
    """
    return a+b