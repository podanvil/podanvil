"""
This is a simple script to create an nginx-based Kubernetes deployment for each loop iteration. 

A config map is used to add dynamic data (the command that was run to create the deployment) to each pod.
"""

import subprocess
from kubernetes import client, config

# Define the base names for your resources
CLUSTER_BASENAME = "clu-rustpress-prod-squeeze-20230731-001"
NODE_BASENAME = "node-rustpress-prod-squeeze-20230731-001"
SERVICE_BASENAME = "svc-rustpress-prod-squeeze-20230731-001"
POD_BASENAME = "pod-rustpress-prod-squeeze-20230731-001"
FILE_NAME = "thaodean.com.tar.gz"

# Define the number of pods
NUMBER_OF_PODS = 58

# Configure kubectl
config.load_kube_config()

# Get the API client
v1 = client.CoreV1Api()

# Loop from 1 to NUMBER_OF_PODS
for i in range(1, NUMBER_OF_PODS + 1):
    # Define the names for this iteration
    CLUSTER = f"{CLUSTER_BASENAME}-{i}"
    NODE = f"{NODE_BASENAME}-{i}"
    SERVICE = f"{SERVICE_BASENAME}-{i}"

    # Define the command
    command = f"python3 podanvil.py {FILE_NAME} -clu {CLUSTER} -node {NODE} -svc {SERVICE}"

    # Create a config map with the command as data
    config_map = client.V1ConfigMap(
        metadata=client.V1ObjectMeta(name=f"command-config-{i}"),
        data={"command": command},
    )
    v1.create_namespaced_config_map("default", config_map)

    # Define the deployment manifest
    deployment = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": f"nginx-deployment-{i}"},
        "spec": {
            "replicas": 1,
            "selector": {"matchLabels": {"app": f"nginx-{i}"}},
            "template": {
                "metadata": {"labels": {"app": f"nginx-{i}"}},
                "spec": {
                    "containers": [
                        {
                            "name": f"nginx-{i}",
                            "image": "nginx:1.14.2",
                            "ports": [{"containerPort": 80}],
                            "volumeMounts": [
                                {
                                    "name": "config-volume",
                                    "mountPath": "/usr/share/nginx/html/index.html",
                                    "subPath": "command",
                                }
                            ],
                        }
                    ],
                    "volumes": [
                        {
                            "name": "config-volume",
                            "configMap": {"name": f"command-config-{i}"},
                        }
                    ],
                },
            },
        },
    }

    # Create the deployment
    client.AppsV1Api().create_namespaced_deployment("default", deployment)

    # Run the original python command as well
    subprocess.run(command, shell=True)

