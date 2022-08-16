import os
import paramiko
import getpass

def sshCommand(ip, port, user, password, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=password)
    junk, stdoutput, stderror = client.exec_command(cmd)
    output = stdoutput.readlines() + stderror.readlines()
    if output:
        print("Output >>> ", end='')
        for line in output:
            print(line.strip())
    sftp_client = client.open_sftp()
    while True:
        path = input("For Data Transfer, Enter path here OR Press Enter to Stop >>> ") or "exit"
        filename = path.split('/')
        file = filename.pop()
        if path == "exit":
            break
        sftp_client.get(path, f"downloaded_data\\{file}")
        print("File downloaded successful!")


if __name__ == '__main__':
    os.system('cls')
    os.system('color 0a')
    user = input("Username: ") or 'zain'
    password = getpass.getpass() or 'zainarif12345'
    ip = input("Enter IP: ") or '192.168.58.128'
    port = input("Enter Port: ") or '22'
    while True:
        cmd = input("Enter Command >>> ")
        if cmd == "exit":
            break
        sshCommand(ip, port, user, password, cmd)

