import os

"""
    Create a directory with the given function name inside the current working directory,
    or return the current directory if no function name is provided.

    Parameters:
    - function_name (str, optional): Name of the directory to be created
    Returns:
    - str: The current directory path if no function name is provided, otherwise None.
    """
def create_directory(function_name=None):
    current_directory = os.getcwd()

    if function_name:
        new_directory = os.path.join(current_directory, function_name)

        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
            print(f"Directory '{function_name}' created at: {new_directory}")
        else:
            print(
                f"Directory '{function_name}' already exists at: {new_directory}")
    else:
        print(f"Current directory: {current_directory}")

    return current_directory if not function_name else None


