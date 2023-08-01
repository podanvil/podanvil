import yaml
import sys

def convert_to_subdomain(url):
    return url.replace('.', '-')

def main():
    url = sys.argv[1]
    subdomain_safe_url = convert_to_subdomain(url)
    
    with open('k8s/ingress_template.yaml', 'r') as f:
        ingress_yaml = yaml.safe_load(f)

    # Replace occurrences in the YAML
    ingress_yaml['metadata']['name'] = f"{subdomain_safe_url}-ingress"
    ingress_yaml['spec']['tls'][0]['hosts'][0] = f"{subdomain_safe_url}.podanvil.com"
    ingress_yaml['spec']['tls'][0]['secretName'] = f"{subdomain_safe_url}-tls"
    ingress_yaml['spec']['rules'][0]['host'] = f"{subdomain_safe_url}.podanvil.com"
    ingress_yaml['spec']['rules'][0]['http']['paths'][0]['backend']['service']['name'] = f"{subdomain_safe_url}-service"

    with open(f'k8s/{subdomain_safe_url}_ingress.yaml', 'w') as f:
        yaml.dump(ingress_yaml, f)

if __name__ == "__main__":
    main()

