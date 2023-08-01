import os
import subprocess
import sys

def compile_rust_to_docker(image_name, rust_file):
    subprocess.run(["cargo", "build", "--release"], check=True)
    subprocess.run(["docker", "build", "--no-cache", "-t", image_name, "."], check=True)

if __name__ == "__main__":
    image_name = sys.argv[1]
    rust_file = sys.argv[2]
    compile_rust_to_docker(image_name, rust_file)

