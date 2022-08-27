# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

REGION = input("Please enter the AWS REGION: ")

# this is the configration for the logger

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

subnet_client = boto3.client("ec2", region_name=REGION)


def create_subnet(az):
    try:
        res = subnet_client.create_default_subnet(AvailabilityZone=az)

    except ClientError:
        logger_for.exception('Oops sorry, Your default subnet is not created:')
        raise
    else:
        return res


if __name__ == '__main__':
    Zone  = input("Enter the availability zone: ")
    logger_for.info(f'Please wait!! Creating default subnet...')
    subnet = create_subnet(Zone)
    logger_for.info(
        f'Wow!!, Your default Subnet is created with ID: \n{json.dumps(subnet, indent=4)}'
    )