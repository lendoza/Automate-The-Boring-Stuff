import os

# Joins files to make directory

files = os.path.join('folder1', 'folder2', 'folder3')

# Gets current working directory

get = os.getcwd()

# Changes directory

change = os.chdir()

# Shows if path/file exists

exist = os.path.exists('spam.png')

# Gives size

size = os.path.size('spam.png')

# Creats new folders

create = os.makedirs('../desktop/walnuts.png')

# . represents this folder

# .. represents the parent folder