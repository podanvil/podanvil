import yaml

def create_deployment(image_name, deployment_name):
    deployment = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": f"{deployment_name}-deployment",
        },
        "spec": {
            "replicas": 1,
            "selector": {
                "matchLabels": {
                    "app": deployment_name,
                },
            },
            "template": {
                "metadata": {
                    "labels": {
                        "app": deployment_name,
                    },
                },
                "spec": {
                    "containers": [
                        {
                            "name": deployment_name,
                            "image": image_name,
                            "ports": [
                                {
                                    "containerPort": 80,
                                },
                            ],
                        },
                    ],
                },
            },
        },
    }

    with open(f"{deployment_name}-deployment.yaml", "w") as f:
        yaml.dump(deployment, f)

# Usage:
create_deployment("your_dockerhub_username/actix_simple_main:latest", "actix_simple_main")
create_deployment("your_dockerhub_username/actix_full_prod_main:latest", "actix_full_prod_main")

