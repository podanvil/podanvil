import argparse
import subprocess
import tarfile
import os

def main():
    parser = argparse.ArgumentParser(description='Run the Podanvil server.')
    parser.add_argument('-tgz', '--tarball', default='helloworld.domain.tar.gz',
                        help='The tarball to serve. Defaults to helloworld.domain.tar.gz.')
    parser.add_argument('-rust', '--rust-server', default='webserver.rust.tar.gz',
                        help='The tarball containing the Rust server code. Defaults to webserver.rust.tar.gz.')

    args = parser.parse_args()

    # Extract the Rust server tarball
    with tarfile.open(args.rust_server, 'r:gz') as tar:
        tar.extractall()

    # Change the binary name to the filename of the Rust server tarball
    binary_name = os.path.splitext(args.rust_server)[0]

    # Update the Dockerfile to use the new binary name
    with open('Dockerfile', 'r') as file:
        dockerfile = file.read()

    dockerfile = dockerfile.replace('/app/target/release/podanvil', f'/app/target/release/{binary_name}')

    with open('Dockerfile', 'w') as file:
        file.write(dockerfile)

    # Run the Docker build command
    subprocess.run(['docker', 'build', '--build-arg', f'URL={args.tarball}', '-t', 'podanvil', '.'])

    # Run the Docker container
    subprocess.run(['docker', 'run', '-p', '80:80', 'podanvil'])

if __name__ == '__main__':
    main()

