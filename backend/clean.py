import os
import shutil

paths_to_remove = ['dist', 'build', '.pytest_cache', '.mypy_cache', 'htmlcov']
files_to_remove = ['.coverage']

for path in paths_to_remove:
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f'🧹📂 Removed directory: {path}')

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f'🧹📁 Removed file: {file}')
