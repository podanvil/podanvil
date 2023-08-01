import subprocess
import sys
import os

def compile_rust_to_docker(image_name, rust_file):
    # Create Dockerfile
    with open("Dockerfile", "w") as f:
        f.write(f"""
        FROM rust:latest as builder
        WORKDIR /usr/src

        COPY ./ ./
        RUN cargo build --release

        FROM debian:buster-slim
        COPY --from=builder /usr/src/target/release/{rust_file} /usr/local/bin
        CMD ["{rust_file}"]
        """)

    # Run Docker build
    subprocess.run(["docker", "build", "-t", image_name, "."], check=True)

if __name__ == "__main__":
    image_name = sys.argv[1]
    rust_file = sys.argv[2]

    # Check that the Rust file exists
    if not os.path.isfile(rust_file):
        print(f"Error: File {rust_file} does not exist.")
        sys.exit(1)

    compile_rust_to_docker(image_name, rust_file)

