import time
import base64
from boto.ec2 import connect_to_region

ec2_conn = connect_to_region("sp-southeast-1")

# create security group allowing SSH
demo_sg = ec2_conn.create_security_group("demo-sg", "Demo Sec Group")
demo_sg.authorize("tcp", 22, 22, "0.0.0.0/0")
demo_sg.authorize("tcp", 80, 80, "0.0.0.0/0")

#create and save a public key for SSH login

demo_key = ec2_conn.create_key_pair("demo-key")
demo_key.save(".")

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
