import boto3
from operator import itemgetter
ec2_client = boto3.client('ec2')

snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self']
)

sorted_del = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'))

for snap in sorted_del[2:]:
   response=ec2_client.delete_snapshot(
   SnapshotId=snap['SnapshotId']
    )

