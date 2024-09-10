FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Gets text file and opens to read content and create and return todos list """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Gets and opens text file to write content, overwriting any existing content, with current todos list"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)