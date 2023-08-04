import os
import subprocess
import tarfile
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} [filename]")
    sys.exit(1)

filename = sys.argv[1]
directory_name = os.path.splitext(os.path.splitext(filename)[0])[0]  # Remove .tar.gz

with tarfile.open(filename, 'r:gz') as tar:
    tar.extractall()

subprocess.check_call(["docker", "build", "-t", "podanvil:latest", "."])
subprocess.check_call(["docker", "tag", "podanvil:latest", "thaodean/podanvil:latest"])
subprocess.check_call(["docker", "push", "thaodean/podanvil:latest"])

# Change this to match your Kubernetes configuration
subprocess.check_call([
    "kubectl", "run", "podanvil",
    "--image=thaodean/podanvil:latest",
    "--", directory_name
])

