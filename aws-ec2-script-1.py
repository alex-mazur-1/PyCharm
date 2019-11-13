
import logging
import boto3
from botocore.exceptions import ClientError

def add_security_group_to_security_group(security_group_id,
                                         source_security_group_name,
                                         source_security_group_owner_id=''):
    """Add a security group to another security group

    Adding a security group to another security group allows traffic
    from EC2 instances associated with the added group.

    For example, assume the following scenario:
      * EC2 instance #1 uses security group #1
      * EC2 instance #2 uses security group #2
    If security group #2 is added to security group #1 then EC2 instance #1
    will accept traffic from EC2 instance #2.

    Traffic is allowed from the private IP addresses of the EC2 instances, not
    the public IP or Elastic IP addresses. All types of traffic are allowed
    (UDP, TCP, and ICMP).

    Note: Adding a security group does not add the group's rules to the
    modified group.

    If a different AWS account owns the added security group then the account
    ID must be specified in the source_security_group_owner_id argument.

    :param security_group_id: ID of the security group to be modified
    :param source_security_group_name: Name of the security group to add
    :param source_security_group_owner_id: AWS account ID that owns the added
    security group. This argument is required only if the modified and added
    security groups are in different AWS accounts.
    :return True if group was added. Otherwise, False.
    """
    # Add the security group
    ec2_client = boto3.client('ec2')
    try:
        ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            SourceSecurityGroupName=source_security_group_name,
            SourceSecurityGroupOwnerId=source_security_group_owner_id)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    """Exercise add_security_group_to_security_group()"""

    # Assign these values before running the program
    security_group_id = 'MODIFIED_SECURITY_GROUP_ID'    # Note: Group ID
    security_group_name = 'ADDED_SECURITY_GROUP_NAME'   # Note: Group Name
    added_security_group_owner_id = ''                  # AWS account ID

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Add the security group to the other security group
    if add_security_group_to_security_group(security_group_id,
                                            security_group_name,
                                            added_security_group_owner_id):
        logging.info(f'Added security group {security_group_name} '
                     f'to security group {security_group_id}')


if __name__ == '__main__':
    main()


# ec2 instance creation

def create_ec2_instance(image_id, instance_type, keypair_name):
    """Provision and launch an EC2 instance

    The method returns without waiting for the instance to reach
    a running state.

    :param image_id: ID of AMI to launch, such as 'ami-XXXX'
    :param instance_type: string, such as 't2.micro'
    :param keypair_name: string, name of the key pair
    :return Dictionary containing information about the instance. If error,
    returns None.
    """
    # Provision and launch the EC2 instance
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.run_instances(ImageId=image_id,
                                            InstanceType=instance_type,
                                            KeyName=keypair_name,
                                            MinCount=1,
                                            MaxCount=1)
    except ClientError as e:
        logging.error(e)
        return None
    return response['Instances'][0]


def main():
    """Exercise create_ec2_instance()"""

    # Assign these values before running the program
    image_id = 'AMI_IMAGE_ID'
    instance_type = 'INSTANCE_TYPE'
    keypair_name = 'KEYPAIR_NAME'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Provision and launch the EC2 instance
    instance_info = create_ec2_instance(image_id, instance_type, keypair_name)
    if instance_info is not None:
        logging.info(f'Launched EC2 Instance {instance_info["InstanceId"]}')
        logging.info(f'    VPC ID: {instance_info["VpcId"]}')
        logging.info(f'    Private IP Address: {instance_info["PrivateIpAddress"]}')
        logging.info(f'    Current State: {instance_info["State"]["Name"]}')


if __name__ == '__main__':
    main()
