import os
import subprocess

url = 'https://dl-cdn.alpinelinux.org/alpine/v3.23/releases/armv7/alpine-minirootfs-3.23.3-armv7.tar.gz'

def run(cmd, cwd=None):
    subprocess.run(cmd, check=True, cwd=cwd)

def download(url, jail_path):
    filename = url.split('/')[-1]
    path = os.path.join(jail_path, filename)

    if os.path.exists(path):
        return filename
    
    run(['wget', url], cwd=jail_path)
    return filename

def extract(archive_name, jail_path):
    if os.path.exists(os.path.join(jail_path, 'bin')):
        return
    
    run(['tar', '-xzf', archive_name], cwd=jail_path)

def child(jail_path):
    os.makedirs(jail_path, exist_ok=True)
    
    archive = download(url, jail_path)
    extract(archive, jail_path)

    os.chroot(jail_path)
    os.chdir('/')

    os.execvp("/bin/sh", ["/bin/sh"])

def main():
    jail_path = "/tmp/linux_jail_root"

    pid = os.fork()
    if pid == 0:
        child(jail_path)
    else:
        os.wait()


if __name__ == "__main__":
    main()




   
