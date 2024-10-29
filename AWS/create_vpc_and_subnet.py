import boto3

ec2_client = boto3.client('ec2')

# Create VPC
vpc = ec2_client.create_vpc(CidrBlock='10.0.0.0/16')

# Create Subnet
subnet = ec2_client.create_subnet(VpcId=vpc['Vpc']['VpcId'], CidrBlock='10.0.1.0/24')

print(vpc)
print(subnet)



