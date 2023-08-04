import subprocess

def run_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    if process.returncode != 0:
        print(f"Failed to execute '{command}'. Error: {process.stderr}")
    else:
        print(process.stdout)

def reset_docker():
    print("Uninstalling Docker...")
    run_command("pacman -Rns --noconfirm docker docker-compose")

    print("Installing Docker...")
    run_command("pacman -Sy --noconfirm docker")

    print("Enabling Docker service...")
    run_command("systemctl enable docker")

    print("Starting Docker service...")
    run_command("systemctl start docker")

    print("Adding current user to Docker group...")
    username = subprocess.check_output('whoami').decode().strip()
    run_command(f"usermod -aG docker {username}")

if __name__ == "__main__":
    reset_docker()

