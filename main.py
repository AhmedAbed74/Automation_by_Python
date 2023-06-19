import boto3

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

new_vpc = ec2_resource.create_vpc(
    CidrBlock="10.0.0.0/16"
)
new_vpc.create_subnet(
    CidrBlock="10.0.1.0/24"
)
new_vpc.create_subnet(
    CidrBlock="10.0.2.0/24"
)

all_avail_vpc = ec2_client.describe_vpcs()
print(all_avail_vpc)
vpcs = all_avail_vpc["Vpcs"]

for a in vpcs:
    print(a["CidrBlock"])
