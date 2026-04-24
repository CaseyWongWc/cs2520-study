from pathlib import Path
import shutil
import subprocess

ROOT = Path.cwd()

def here():
    return ROOT

def make_dir(path):
    p = ROOT / path
    p.mkdir(parents=True, exist_ok=True)
    return p

def make_file(path, content=""):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return p

def remove_path(path):
    p = ROOT / path
    if p.is_dir():
        shutil.rmtree(p)
    elif p.exists():
        p.unlink()
    return p

def run_cmd(*cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode

print("Current working directory:", here())

# Examples:
# make_dir("demo/subfolder")
# make_file("demo/subfolder/hello.txt", "hello from notebook
Hey.")
# run_cmd("find", "demo", "-maxdepth", "3")
# remove_path("demo")