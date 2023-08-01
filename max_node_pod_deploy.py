"""
This is an example usage of the podanvil.py script.

It demonstrates how to use podanvil.py to start a specific number of pods 
on different nodes. Specifically, it starts 58 pods, each on a separate node.

In this script, it starts all of the numbered pods with deployments and services,
and nginx ingress controller rules to direct incoming service traffic to the service and from there to the pod. 
The domain name is currently encoded in the file name (e.g., thaodean.com.tar.gz),
so here thaodean.com is the domain, and the ingress controller directs incoming traffic to this domain to the service 
(svc-rustpress-prod-squeeze-20230731-001), which serves it from the pod. 
Since on a squeeze cluster or squeeze mode deployments by default are started with a single pod for efficiency.

This script is meant to be run in an environment where you have permission to create resources on AWS and 
where podanvil.py is available.
"""

import subprocess

# Define the base names for your resources
CLUSTER_BASENAME = "clu-rustpress-prod-squeeze-20230731-001"
NODE_BASENAME = "node-rustpress-prod-squeeze-20230731-001"
SERVICE_BASENAME = "svc-rustpress-prod-squeeze-20230731-001"
POD_BASENAME = "pod-rustpress-prod-squeeze-20230731-001"
FILE_NAME = "thaodean.com.tar.gz"

# Define the number of pods
NUMBER_OF_PODS = 58

# Loop from 1 to NUMBER_OF_PODS
for i in range(1, NUMBER_OF_PODS + 1):
    # Define the names for this iteration
    CLUSTER = f"{CLUSTER_BASENAME}-{i}"
    NODE = f"{NODE_BASENAME}-{i}"
    SERVICE = f"{SERVICE_BASENAME}-{i}"

    # Run the python command
    command = f"python3 podanvil.py {FILE_NAME} -clu {CLUSTER} -node {NODE} -svc {SERVICE}"
    subprocess.run(command, shell=True)

