import time
import base64
from boto.ec2 import connect_to_region

ec2_conn = connect_to_region("sp-southeast-1")


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
