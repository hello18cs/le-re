import subprocess

num_containers = 3
image_name = "nginx"
base_name = "scalable_container"

print(f"Deploying {num_containers} containers using image '{image_name}'...\n")

subprocess.run(["docker", "pull", image_name])

for i in range(num_containers):
    container_name = f"{base_name}_{i+1}"
    subprocess.run(["docker", "run", "-d", "--name", container_name, image_name])
    print(f"Started container: {container_name}")

print("\nAll containers deployed successfully")

print("Currently running containers:\n")
subprocess.run(["docker", "ps"])

print("\nStopping and removing containers...")

for i in range(num_containers):
    container_name = f"{base_name}_{i+1}"
    subprocess.run(["docker", "stop", container_name])
    subprocess.run(["docker", "rm", container_name])
    print(f"Removed container: {container_name}")

print("\nCleanup complete!")
