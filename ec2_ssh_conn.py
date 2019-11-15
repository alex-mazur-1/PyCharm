import boto3

import botocore

import paramiko

key = paramiko.RSAKey.from_private_key_file(path / to / mykey.pem)

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy()


def ssh_login(self):

    try:
        cert = paramiko.RSAKey.from_private_key_file("key.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print "connecting..."
        c.connect( hostname = "9.0.0.0", username = "example", pkey = cert )
        print "connected!!!"
        stdin, stdout, stderr = c.exec_command('ls')
        print stdout.readlines()
        c.close()

    except:
        print("Connection Failed!!!")
