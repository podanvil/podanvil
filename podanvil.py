# podanvil.py

import subprocess
import os
import logging

logging.basicConfig(level=logging.INFO)

def deploy(file_name, cluster=None, node=None, service=None, pod=None):
    """
    This function deploys a pod to a node and returns the URL of the pod.
    """
    # Validate the file
    if not os.path.isfile(file_name):
        logging.error(f"File {file_name} does not exist.")
        return

    # If the parameters are not provided, generate them
    cluster = cluster or generate_name(file_name, "cluster")
    node = node or get_active_node()  # Ask the user if it's okay to use the active node
    service = service or generate_name(file_name, "service")
    pod = pod or generate_name(file_name, "pod")

    try:
        # Deploy the pod (implementation is not shown)
        deploy_pod(file_name, cluster, node, service, pod)

        # Get the URL of the pod
        url = get_pod_url(cluster, service, pod)

        # Verify the pod is accessible
        if not is_accessible(url):
            raise Exception(f"Failed to access {url}")
    except Exception as e:
        logging.error(f"Failed to deploy pod. Reason: {str(e)}")
        return

    return url

# Rest of the functions stay the same

