import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RPATOOL = os.path.join(BASE_DIR, "rpatool.py")

def extract_rpa(rpa_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    subprocess.run(
        [sys.executable, RPATOOL, "-x", rpa_file, "-o", output_dir],
        check=True
    )

def decompile_rpyc(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    subprocess.run(
        [sys.executable, "-m", "unrpyc", input_dir, "-o", output_dir],
        check=True
    )
