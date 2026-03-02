import sys
import os
import subprocess

# 1. Fork the parent process
pid = os.fork()
jail = 'linux_jail_root'

# 2. Exec into the new process
if pid == 0:
    print(os.getpid())
    listing = os.execv("/bin/echo", ['echo', 'Hello World'])
    print(listing)
else:
    os.wait()

# Creating jail directory and switching to it:
os.mkdir(jail)
subprocess.run(['cd', jail])
    

# 3. Grab mini linux from web

mini_linux_link = 'https://dl-cdn.alpinelinux.org/alpine/v3.23/releases/armv7/alpine-minirootfs-3.23.3-armv7.tar.gz'

def download_item(link):
    try:
        subprocess.run(['wget', link])
    except subprocess.CalledProcessError as e:
        print("wget failed")
        print(f"Exit code: {e.returncode}")
    except subprocess.SubprocessError:
        print("wget is not installed or path is not found")
    except subprocess.TimeoutExpired:
        print('wget timed out. Trying againing')

        
        

        

# 4. Create jail directory:
#   - mkdir jail file and switch to it
#   - decompress mini linux inside file







