
import logging
import boto3
from botocore.exceptions import ClientError

# EC2 Tag attachment

#ec2 = boto3.client('ec2')
#tag = ec2.Tag('resource_id', 'EC2', '123321')



# ec2 instance creation

def create_ec2_instance(image_id, instance_type, keypair_name):

    # Provision and launch the EC2 instance
    # The method returns without waiting for the instance to reach
    # a running state. If error, returns None.
    ec2 = boto3.client('ec2')
    try:
        response = ec2.run_instances(ImageId=image_id,
                                     InstanceType=instance_type,
                                     KeyName=keypair_name,
                                     #SecurityGroupIds=["security_group_id"],
                                     MinCount=1,
                                     MaxCount=1)
    except ClientError as e:
        logging.error(e)
        return None
    return response['Instances'][0]


def main():

    # Assign the values
    image_id = 'ami-028188d9b49b32a80'
    instance_type = 't2.micro'
    keypair_name = 'SSH_KEY_PAIR'


    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    instance_info = create_ec2_instance(image_id, instance_type, keypair_name)
    if instance_info is not None:
        logging.info(f'Launched EC2 Instance {instance_info["InstanceId"]}')
        logging.info(f'    VPC ID: {instance_info["VpcId"]}')
       #logging.info(f'    GroupId: {instance_info["security_group_id"]}')
        logging.info(f'    Private IP Address: {instance_info["PrivateIpAddress"]}')
        logging.info(f'    Current State: {instance_info["State"]["Name"]}')

if __name__ == '__main__':
    main()
