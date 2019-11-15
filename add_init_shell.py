import time
import os
import sys
import base64
#from boto.ec2 import connect_to_region


ec2_conn = connect_to_region("us-west-1")


# Base64 and save a public key for SSH login.
with open('init.sh') as f:
    userdata = f.read()

# create the instance using AMIN Linux
resrv = ec2_conn.run_instances("ami-fade9la8",
                               key_name="demo-key",
                               instance_type="t2.micro",
                               security_groups=["demo-sg"],
                               user_data=userdata)
# get the demo instance IP address,
demo = resrv.instances[0]
while demo.update() != 'running':
    time.sleep(1)
print(demo.ip_address)


conn = boto.ec2.connect_to_region("us-west-1")

myCode = """#!/bin/bash
sudo mkfs.ext4 /dev/xvdf
sudo mkdir /vol
echo "/dev/xvdf /vol auto noatime 0 0" | sudo tee -a /etc/fstab"""

#### creating a new instance ####
new_reservation = conn.run_instances("ami-d16a8b95",
    key_name="bogo",
    instance_type="t1.micro",
    security_group_ids=["sg-0841236d"],
    user_data=myCode
    )

instance = new_reservation.instances[0]