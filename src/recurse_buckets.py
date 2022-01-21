from unicodedata import name
import boto3

s3_client = boto3.client('s3')

def list_buckets():
    response = s3_client.list_buckets()
    bucket_list = response["Buckets"]
    while "NextToken" in response:
        response = s3_client.list_buckets(NextToken=response["NextToken"])
        bucket_list.extend(response["Buckets"])

    for bucket in bucket_list:
        bucket_name = bucket['Name']
        print(f"Bucket Name: {bucket_name}")
        # {'Name': 'builds-astech-io', 'CreationDate': datetime.datetime(2020, 9, 7, 3, 44, 18, tzinfo=tzutc())}
        paginator = s3_client.get_paginator('list_objects')
        for result in paginator.paginate(Bucket=f'{bucket_name}', Delimiter='/'):
            prefix_list = []
            prefix_list = result.get('CommonPrefixes')
            if prefix_list:
                print("prefix list:")
                for prefix in prefix_list:
                    print(f"    {prefix['Prefix']}")
            else:
                print(f"Bucket {bucket_name} doesn't have folders")
        print()

if __name__ == "__main__":
    list_buckets()