import sys
import subprocess

subprocess.run([sys.executable, "-m", "pip", "install", "scamp"])

try:
    import scamp
    print("Scamp is now installed and imported.")
except ImportError:
    print("Scamp installation failed. Try installing manually.")
