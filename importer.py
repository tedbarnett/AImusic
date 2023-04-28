# importer.py

import sys
import subprocess

print("Running importer.py")

# Install abjad (pip3 install abjad==3.4) v3.4 required for Scamp apparently
subprocess.run([sys.executable, "-m", "pip", "install", "abjad==3.4"])

try:
    import abjad
    print("abjad is now installed and imported.")
except ImportError:
    print("abjad installation failed. Try installing manually.")

# Now install scamp
subprocess.run([sys.executable, "-m", "pip", "install", "scamp"])

try:
    import scamp
    print("Scamp is now installed and imported.")
except ImportError:
    print("Scamp installation failed. Try installing manually.")


# Now install scamp_extensions
subprocess.run([sys.executable, "-m", "pip", "install", "scamp_extensions"])

try:
    import scamp_extensions
    print("scamp_extensions is now installed and imported.")
except ImportError:
    print("scamp_extensions installation failed. Try installing manually.")


# Now install music21
subprocess.run([sys.executable, "-m", "pip", "install", "music21"])

try:
    import music21
    print("music21 is now installed and imported.")
except ImportError:
    print("music21 installation failed. Try installing manually.")
