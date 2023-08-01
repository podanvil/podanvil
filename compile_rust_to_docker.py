import os
import subprocess
import sys

RUST_BINARY = "podanvil"
RUST_VERSION = "latest"
DEBIAN_VERSION = "buster-slim"

def create_dockerfile():
    with open("Dockerfile", "w") as f:
        f.write(f"""
        FROM rust:{RUST_VERSION} as builder
        WORKDIR /usr/src

        COPY ./ ./
        RUN cargo build --release

        FROM debian:{DEBIAN_VERSION}
        COPY --from=builder /usr/src/target/release/{RUST_BINARY} /usr/local/bin/{RUST_BINARY}
        CMD ["/usr/local/bin/{RUST_BINARY}"]
        """)

def compile_rust_to_docker(image_name):
    subprocess.run(["cargo", "build", "--release"], check=True)
    subprocess.run(["docker", "build", "--no-cache", "-t", image_name, "."], check=True)

if __name__ == "__main__":
    image_name = sys.argv[1]
    create_dockerfile()
    compile_rust_to_docker(image_name)

