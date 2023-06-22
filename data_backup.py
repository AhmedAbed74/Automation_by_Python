import boto3
import schedule
import datetime

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

# use can user describe_volumes() instead and become  faster
ins = ec2_client.describe_instances()


def automatic_backup():
    for x in ins['Reservations']:
        block_id = x['Instances']
        for y in block_id:
            sys_status = y['BlockDeviceMappings']
            for z in sys_status:
                ebs_id = z['Ebs']
                response = ec2_client.create_snapshot(
                    VolumeId=ebs_id['VolumeId']
                )
                print(response)
                x = datetime.datetime.now()
                print(x)


def easy_automatic_backup():
    volumes = ec2_client.describe_volumes()
    for vol in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=vol['VolumeId']
        )
        print(new_snapshot)
        x = datetime.datetime.now()
        print(x)


schedule.every(1).minutes.do(easy_automatic_backup)

while True:
    schedule.run_pending()
