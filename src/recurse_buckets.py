from unicodedata import name
import boto3

s3_client = boto3.client('s3')

def list_buckets():
    response = s3_client.list_buckets()
    bucket_list = response["Buckets"]
    while "NextToken" in response:
        response = s3_client.list_buckets(NextToken=response["NextToken"])
        bucket_list.extend(response["Buckets"])

    # with open('xmen.txt', 'w+') as my_file:
    with open('bucket_and_prefixes.txt', 'w') as bucketfile:
        for bucket in bucket_list:
            bucket_name = bucket['Name']
            print(f"Bucket Name: {bucket_name}")
            bucketfile.write(f"Bucket name: {bucket_name}\n")
            paginator = s3_client.get_paginator('list_objects')
            for result in paginator.paginate(Bucket=f'{bucket_name}', Delimiter='/'):
                prefix_list = []
                prefix_list = result.get('CommonPrefixes')
                if prefix_list:
                    print("prefix list:")
                    bucketfile.write(f"prefix list:\n")
                    for prefix in prefix_list:
                        bucketfile.write(f"    {prefix['Prefix']}\n")
                        print(f"    {prefix['Prefix']}")
                else:
                    print(f"Bucket {bucket_name} doesn't have folders")
                    bucketfile.write(f"    Bucket {bucket_name} doesn't have folders\n")
        print()

if __name__ == "__main__":
    list_buckets()