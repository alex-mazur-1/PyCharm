import boto3

# keypair creation  +save

ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName='SSH_KEY2_PAIR')
print(response)
#response.save(".")