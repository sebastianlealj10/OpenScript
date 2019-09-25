import os


def get_description():
    dir_path = os.getcwd()
    dir_path = dir_path.replace('Scripts', '')
    f = open(dir_path + 'Description', 'r')
    description = f.read()
    return description
