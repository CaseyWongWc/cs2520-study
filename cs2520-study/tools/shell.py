def run_shell_command(command):
    import subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def list_directory(path='.'):
    import os
    return os.listdir(path)

def change_directory(path):
    import os
    os.chdir(path)

def create_directory(path):
    import os
    os.makedirs(path, exist_ok=True)

def remove_directory(path):
    import shutil
    shutil.rmtree(path)

def execute_command(command):
    stdout, stderr = run_shell_command(command)
    if stderr:
        print(f"Error: {stderr}")
    return stdout.strip()