# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def create_default_subnet(az):
    try:
        response = vpc_client.create_default_subnet(AvailabilityZone=az)

    except ClientError:
        logger.exception('can not create default subnet.')
        raise
    else:
        return response


if __name__ == '__main__':
    AvailabilityZone = input("Enter the availability zone")
    logger.info(f'Please wait!! Creating default subnet...')
    default_subnet = create_default_subnet(AvailabilityZone)
    logger.info(
        f'Wow!!, Your default Subnet is created with ID: \n{json.dumps(default_subnet, indent=4)}'
    )