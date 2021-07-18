from Ping_ import Ping
#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
import paramiko
import time
def SSH(ip,username,password):
# ip = "192.168.0.128"
# username = "hillstone"
# password = "hillstone"
    ssh_client =paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password)
    print("Successfully connected to" ,ip)
    command = ssh_client.invoke_shell()
    command.send("configure\n")
    command.send("show interface\n")
    time.sleep(2)
    output = command.recv(65535)
    print(output.decode("ascii"))
    ssh_client.close()
if __name__ == "__main__":
    result = Ping("111.111.111.111")
    # Ping("192.168.0.130")
    if result ==1:
        SSH("111.111.111.111","hillstone","hillstone")
    if result ==0:
        print("Ping不通，无法SSH登录")

