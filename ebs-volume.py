import boto3
import boto3.ec2
import sys

client = boto3.client('ec2')
# create an EBS volume, 1G size

ebs_vol = client.create_volume(
    AvailabilityZone='symphony',
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
volume_id = ebs_vol['VolumeId']

#check that the EBS volume has been created successfully
if ebs_vol['ResponseMetadata']['HTTPStatusCode'] == 200:
        print ("Successfully created Volume! ") + volume_id

 attaching EBS volume to our EC2 instance
    attach_resp = client.attach_volume(
        VolumeId=volume_id,
        InstanceId=ec2_instance['Instances'][0]['InstanceId'],
        Device='/dev/xvdf')

if __name__ == '__main__':
sys.exit(main(sys.argv[1:]))
