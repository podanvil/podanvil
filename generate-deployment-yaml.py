import sys

def convert_to_subdomain(url):
    return url.replace('.', '-')

def main():
    url = sys.argv[1]
    subdomain_safe_url = convert_to_subdomain(url)

    with open('k8s/ingress_template.yaml', 'r') as f:
        ingress_yaml = f.read()

    # Replace placeholders in the YAML
    ingress_yaml = ingress_yaml.replace('{{subdomain_safe_url}}', subdomain_safe_url)

    with open(f'k8s/{subdomain_safe_url}_ingress.yaml', 'w') as f:
        f.write(ingress_yaml)

if __name__ == "__main__":
    main()

