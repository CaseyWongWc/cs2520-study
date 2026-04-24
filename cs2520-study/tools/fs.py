def create_file(path, content=""):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def delete_file(path):
    import os
    if os.path.exists(path):
        os.remove(path)

def list_directory(path):
    import os
    return os.listdir(path)

def create_directory(path):
    import os
    os.makedirs(path, exist_ok=True)

def delete_directory(path):
    import shutil
    if os.path.exists(path):
        shutil.rmtree(path)