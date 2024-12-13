try:
    # Code with incorrect indentation in a string
    code_with_error = """
def sample_function():
print("This will cause an IndentationError")
"""
    # Attempt to execute the code with incorrect indentation
    exec(code_with_error)
except IndentationError:
    print("IndentationError: Code is not properly indented.")
