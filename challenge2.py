import boto3
import json

#Queries metadata of EC2 instance of your choice and prints the JSON formatted output
instance = input("Enter instance id to fetch metadata: ")
def get_metadata(instance_id):
    client = boto3.client('ec2', region_name="us-east-1")
    response = client.describe_instances(InstanceIds=[instance_id]).get("Reservations")
    #print(type(response)) #This will print type asdict
    json_string = json.dumps(response, indent=2, default=str)
    print(json_string)

get_metadata(instance)

#Retrieves the data of your choice
data = input("Enter data key to be retrieved: ")
def get_data_key(data):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances().get("Reservations")
    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get(data))

get_data_key(data)
