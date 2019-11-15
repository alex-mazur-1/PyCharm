import boto3
import time

ec2 = boto3.resource('ec2')

#### Create a volume ####

vol = ec2.create_volume(
   AvailabilityZone='eu-west-1c',
      Size=1,
      VolumeType='standard',
      TagSpecifications=[
         {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'TAG',
                    'Value': '1234567'
                },
            ]
         },
      ]
   )
print ('Volume Id: ', vol.id)

# "check that the EBS volume has been created successfully"

time.sleep(15)

#### Attach a volume ####
ec2 = boto3.resource('ec2')
result = vol.attach_to_instance(Device='/dev/xvdf', InstanceId = 'i-0409822b9dae33c7a')
print ('Attach Volume Result: ', result)