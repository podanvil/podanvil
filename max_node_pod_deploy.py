"""
This is an example usage of the podanvil.py script.

It demonstrates how to use podanvil.py to start a specific number of pods on a single node.

This script is meant to be run in an environment where you have permission to create resources on AWS and
where podanvil.py is available.
"""

import subprocess

# Define the base names for your resources
CLUSTER = "clu-rustpress-prod-squeeze-20230731-001"
NODE = "node-rustpress-prod-squeeze-20230731-001"
SERVICE = "svc-rustpress-prod-squeeze-20230731-001"
POD_BASENAME = "pod-rustpress-prod-squeeze-20230731-001"
FILE_NAME = "thaodean.com.tar.gz"

# Define the number of pods
NUMBER_OF_PODS = 58

# Loop from 1 to NUMBER_OF_PODS
for i in range(1, NUMBER_OF_PODS + 1):
    # Define the pod name for this iteration
    POD = f"{POD_BASENAME}-{i}"

    # Run the python command
    command = f"python3 podanvil.py {FILE_NAME} -clu {CLUSTER} -node {NODE} -svc {SERVICE} -pod {POD}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    stdout, _ = process.communicate()

    # Check for errors
    if process.returncode != 0:
        print(f"Failed to deploy pod {POD} to {NODE}.")
    else:
        # Print the returned URL
        print(f"Deployed pod {POD} to {NODE}. The site can be accessed at {stdout.decode().strip()}")

