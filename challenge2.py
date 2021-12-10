import boto3
import json

#Queries metadata of EC2 instance and prints the JSON formatted output
client = boto3.client('ec2', region_name="us-east-1")
response = client.describe_instances()
print(type(response)) #This will print type as dict
json_string = json.dumps(response, indent=2, default=str)
print(json_string)

#Get data key of your choice
data = input("Enter data key to be retrieved: ")
def get_data(data):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances().get("Reservations")
    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get(data))

get_data(data)
