
#!/usr/bin/env python3

import os
import sys
import subprocess

def compile_rust_to_docker(image_name, rust_file):
    # 1. Compile Rust code to binary using cargo
    subprocess.run(["cargo", "build", "--release"], check=True)

    # 2. Write a simple Dockerfile to use the compiled binary
    dockerfile_content = f"""
    FROM scratch
    COPY ./target/release/{rust_file} /
    CMD ["/{rust_file}"]
    """
    with open('Dockerfile', 'w') as file:
        file.write(dockerfile_content)

    # 3. Build Docker image
    subprocess.run(["docker", "build", "-t", image_name, "."], check=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: compile-rust.py <image-name> <rust-file>")
        sys.exit(1)
    
    image_name = sys.argv[1]
    rust_file = sys.argv[2]

    compile_rust_to_docker(image_name, rust_file)


