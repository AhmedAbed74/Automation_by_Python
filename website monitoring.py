import requests
import smtplib
import os
import paramiko
import boto3

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
url = "http://52.55.93.152:8080/"
ec2_client = boto3.client('ec2')
hostname = "52.55.93.152"
instance_id = "i-06b18ea1db2de7fd7"


def send_notification(email_message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        msg = f"site down {email_message}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, "Subject : Site down please fix it")


def restart_app():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=hostname, username="ec2-user", key_filename='C:/Users/Egy Sky/Desktop/blabla.pem')
    stdin, stdout, stderr = ssh.exec_command('docker start 0eca6cd322ae')
    print(stdout.readlines())
    ssh.close()
    print("Application restarted")


try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Application is running successfully ! ")
    else:
        print("Application down,"
              "Fix it ")
        mssg = f'application return {response.status_code}'
        # send email
        send_notification(mssg)
        # restart the app
        restart_app()
except Exception as ex:
    print(f"connection Erorr {ex} ")
    mssg2 = f"server maybe down {ex}"
    send_notification(mssg2)

    # restart aws server
    response = ec2_client.reboot_instances(
        InstanceIds=[
            instance_id,
        ]
    )
    # restart the container
    restart_app()
