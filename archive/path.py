import os
import pathlib
import tempfile

try:
    os.makedirs("config")
except FileExistsError:
    # directory already exists
    pass

os.system('token.py')

