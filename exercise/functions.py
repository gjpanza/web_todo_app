import os
#FILEPATH = r"D:\Python Mega\Examples\app1\files\todo.txt"
FILEPATH="todo.txt"
   
if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass

def get_todos(filepath=FILEPATH):
    """  Reads a file and returns list of to-dos """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos( todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

