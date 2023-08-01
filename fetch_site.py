import subprocess
import sys

def fetch_website(url):
    domain_name = url.split('//')[-1].split('/')[0]
    output_file = f"{domain_name}.tar.gz"
    command = f"wget --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --domains {domain_name} --no-parent {url} && tar -czvf {output_file} {domain_name}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_website(url)

