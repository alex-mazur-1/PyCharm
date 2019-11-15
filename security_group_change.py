import logging
import boto3
from botocore.exceptions import ClientError

def change_instance_security_groups(instance_id, security_group_ids):
    """Change the security groups assigned to an EC2 instance

    This method assigns the security groups to each elastic network interface
    attached to the EC2 instance.

    :param instance_id: EC2 instance ID
    :param security_group_ids: list of security group IDs
    :return True if the security groups were assigned to each network interface
    in the EC2 instance. Otherwise, False.
    """

    # Retrieve the IDs of the network interfaces attached to the EC2 instance
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
    except ClientError as e:
        logging.error(e)
        return False
    instance_info = response['Reservations'][0]['Instances'][0]

    # Assign the security groups to each network interface
    for network_interface in instance_info['NetworkInterfaces']:
        try:
            ec2_client.modify_network_interface_attribute(
                NetworkInterfaceId=network_interface['NetworkInterfaceId'],
                Groups=security_group_ids)
        except ClientError as e:
            logging.error(e)
            return False
    return True


def main():
    """Exercise change_instance_security_groups()"""

    # Assign these values before running the program
    ec2_instance_id = 'i-0409822b9dae33c7a'
    security_group_ids = [
        'sg-0e9697b2a6899f513'
    ]

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Assign the security groups to the EC2 instance
    if change_instance_security_groups(ec2_instance_id, security_group_ids):
        logging.info(f'Changed EC2 Instance {ec2_instance_id} Security Groups to:')
        for security_group in security_group_ids:
            logging.info(f'    ID: {security_group}')


if __name__ == '__main__':
    main()