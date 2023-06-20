import boto3

ec2_client = boto3.client('ec2')
ec2_client2 = boto3.client('ec2', region_name = "us-east-1")

ec2_resource = boto3.resource('ec2')

NorthVirginia = ec2_client.describe_instances()['Reservations']
frankfurt = ec2_client2.describe_instances()['Reservations']
instance_id_NorthVirginia= []
instance_id_frankfurt = []

for ami in NorthVirginia:
    x = ami['Instances']
    for y in x:
        print(y['InstanceId'])

for ami2 in frankfurt:
    x = ami2['Instances']
    for y in x:
        print(y['InstanceId'])

ec2_client.create_tags(
    Resources=[
      'i-00676dc4066cd31a2',
      'i-05909f08327eb02d0',
    ],
    Tags=[
        {
        'Key': 'ENV',
        'Value': 'dev' },
    ]
)
ec2_client2.create_tags(
    Resources=[
      'i-0c77a1e9f6e7973ab',
    ],
    Tags=[
        {
        'Key': 'ENV',
        'Value': 'deploy' },
    ]
)

