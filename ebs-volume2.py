import boto3
import time

ec2 = boto3.resource('ec2')

#### Create a volume ####
# create_volume(size, zone, snapshot=None, volume_type=None, iops=None)
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

# Add a Name tag to the new volume so we can find it.
ec2.create_tags([vol.id], "Name")

# We can check if the volume is now ready and available:
curr_vol = ec2.get_all_volumes([vol.id])[0]
while curr_vol.status == 'creating':
      curr_vol = ec2.get_all_volumes([vol.id])[0]
      print ('Current Volume Status: ', curr_vol.status)
      time.sleep(2)
print ('Current Volume Zone: ', curr_vol.zone)


#### Attach a volume ####
result = ec2.attach_volume (vol.id, instance.id, "/dev/sdf")
print ('Attach Volume Result: ', result)