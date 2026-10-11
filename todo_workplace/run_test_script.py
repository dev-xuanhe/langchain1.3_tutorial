import subprocess
import sys

result = subprocess.run([sys.executable, "-m", "pytest", "-v", "test_my_add.py"], capture_output=True, text=True)
print("STDOUT:")
print(result.stdout)
print("STDERR:")
print(result.stderr)
print(f"Return code: {result.returncode}")
