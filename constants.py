import os


current_path  =  str(os.path.abspath(os.getcwd()))

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

print(ROOT_DIR)