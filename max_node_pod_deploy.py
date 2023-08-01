# max_node_pod_deploy.py

import podanvil
import logging

logging.basicConfig(level=logging.INFO)

# Define the number of pods to deploy
NUMBER_OF_PODS = 58

def deploy_pods():
    """
    This function deploys a specified number of pods to a node.
    """
    # Define the base names for your resources
    CLUSTER_BASENAME = "clu-rustpress-prod-squeeze-20230731-001"
    NODE_BASENAME = "node-rustpress-prod-squeeze-20230731-001"
    SERVICE_BASENAME = "svc-rustpress-prod-squeeze-20230731-001"
    POD_BASENAME = "pod-rustpress-prod-squeeze-20230731-001"
    FILE_NAME = "thaodean.com.tar.gz"

    # Loop from 1 to NUMBER_OF_PODS
    for i in range(1, NUMBER_OF_PODS + 1):
        # Define the names for this iteration
        CLUSTER = f"{CLUSTER_BASENAME}"
        NODE = f"{NODE_BASENAME}"
        SERVICE = f"{SERVICE_BASENAME}-{i}"
        POD = f"{POD_BASENAME}-{i}"

        # Run the podanvil deploy function
        url = podanvil.deploy(FILE_NAME, CLUSTER, NODE, SERVICE, POD)
        if url:
            logging.info(f"The contents of {FILE_NAME} are available on {url}")
        else:
            logging.warning("Deployment failed. Moving to the next pod.")

if __name__ == "__main__":
    deploy_pods()


