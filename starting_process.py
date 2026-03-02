import sys
import os
import subprocess

mini_linux_link = 'https://dl-cdn.alpinelinux.org/alpine/v3.23/releases/armv7/alpine-minirootfs-3.23.3-armv7.tar.gz'


# 1. Fork the parent process
pid = os.fork()
jail = 'linux_jail_root'

# 2. Exec into the new process
if pid == 0:
    os.makedirs(f'/tmp/{jail}', exist_ok=True)

    def download_item(link):
        try:
            subprocess.run(['wget', mini_linux_link], check=True, cwd=f'/tmp/{jail}/')
        except subprocess.CalledProcessError as e:
            print("wget failed")
            print(f"Exit code: {e.returncode}")
        except subprocess.SubprocessError:
            print("wget is not installed or path is not found")
        except subprocess.TimeoutExpired:
            print('wget timed out. Trying againing')

    download_item(mini_linux_link)
else:
    os.wait()

# Creating jail directory and switching to it:

    

# 3. Grab mini linux from web




        
        

        

# 4. Create jail directory:
#   - mkdir jail file and switch to it
#   - decompress mini linux inside file







