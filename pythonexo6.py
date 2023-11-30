import subprocess
import sys

# Ensure a repository name is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script.py <exo6>")
    sys.exit(1)

exo6 = sys.argv[1]

# Run Terraform apply with the desired repository name as a variable
subprocess.run(["terraform", "apply", "-auto-approve", f"-var='exo6={exo6}'"])

