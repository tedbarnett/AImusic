#  Pinstall_lilypond_macos.py
# LILYPOND_URL = "https://gitlab.com/lilypond/lilypond/-/releases/v2.24.1/downloads/lilypond-2.24.1-darwin-x86_64.tar.gz"

import os
import sys
import requests
import subprocess
import tempfile
import tarfile

LILYPOND_URL = "https://gitlab.com/lilypond/lilypond/-/releases/v2.24.1/downloads/lilypond-2.24.1-darwin-x86_64.tar.gz"

def download_lilypond(url):
    resp = requests.get(url)
    resp.raise_for_status()
    
    with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as f:
        f.write(resp.content)
        return f.name

def install_lilypond(tar_path):
    with tempfile.TemporaryDirectory() as temp_dir:
        with tarfile.open(tar_path, "r:gz") as t:
            t.extractall(temp_dir)
        
        # Find 'lilypond' (not LilyPond.app) binary in the extracted files
        lilypond_binary = None
        for dirpath, dirnames, filenames in os.walk(temp_dir):
            if 'lilypond' in filenames:
                lilypond_binary = os.path.join(dirpath, 'lilypond')
                break

        if lilypond_binary is None:
            print("Error: Couldn't find 'lilypond' binary in the extracted files", file=sys.stderr)
            sys.exit(1)

        install_dir = "/usr/local/bin"

        exit_code = subprocess.call(['cp', lilypond_binary, install_dir])
        if exit_code != 0:
            print("Error: Couldn't install LilyPond", file=sys.stderr)
            sys.exit(1)


def set_path():
    shell = os.environ["SHELL"]
    profile_name = ".bash_profile" if "bash" in shell else ".zprofile"
    profile_path = os.path.join(os.path.expanduser("~"), profile_name)

    with open(profile_path, "a") as f:
        f.write('\nexport PATH="/Applications/LilyPond.app/Contents/Resources/bin:$PATH"')

    os.execv(shell, [shell])

def main():
    print("Downloading LilyPond...")
    tar_path = download_lilypond(LILYPOND_URL)

    print("Installing LilyPond...")
    install_lilypond(tar_path)

    print("Setting PATH...")
    set_path()

if __name__ == "__main__":
    main()
