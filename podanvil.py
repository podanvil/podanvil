# This script manages your Docker environment and streamlines the build and deployment of your PaaS infrastructure using Kubernetes.
# You can run this script without parameters for default behaviour, which will build the Docker image for the project with the tag "podanvil:latest".
# To build the Docker image with a custom tag, use the '-t' or '--tag' option:
# python3 podanvil.py --tag my-custom-tag
# To clean your Docker environment, use the '-c' or '--clean' option:
# python3 podanvil.py --clean

import argparse
import subprocess
import sys
from datetime import datetime

DEFAULT_IMAGE_TAG = "podanvil:latest"
DEFAULT_REPLICAS = 3

def build_image(tag):
    print(f"Building Docker image with tag: {tag}")
    subprocess.run(["docker", "build", "-t", tag, "-f", "Dockerfile.rust", "."], check=True)

def deploy_to_kubernetes(tag, replicas):
    print(f"Deploying Docker image '{tag}' to Kubernetes with {replicas} replicas")
    # Kubernetes deployment commands would go here

def clean_docker_environment():
    print("Cleaning Docker environment")
    # Docker cleanup commands would go here

def main():
    parser = argparse.ArgumentParser(description="Manage your Docker environment and Kubernetes deployments.")
    parser.add_argument("-t", "--tag", default=DEFAULT_IMAGE_TAG, help="The tag to use when building the Docker image. Defaults to 'podanvil:latest'.")
    parser.add_argument("-r", "--replicas", type=int, default=DEFAULT_REPLICAS, help="The number of replicas to use when deploying to Kubernetes. Defaults to 3.")
    parser.add_argument("-c", "--clean", action='store_true', help="If specified, cleans the Docker environment before building the image and deploying.")

    args = parser.parse_args()

    if args.clean:
        clean_docker_environment()

    build_image(args.tag)

    deploy_to_kubernetes(args.tag, args.replicas)

if __name__ == "__main__":
    main()

