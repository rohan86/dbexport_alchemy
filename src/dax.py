Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@rohan86 
linuxacademy
/
content-dynamodb-deepdive
8
3538
Code
Pull requests
Actions
Projects
Security
Insights
content-dynamodb-deepdive/6.3.1-Static-Data-Dumps/create_leaderboard.py /
@mrichman
mrichman Removed LSI
Latest commit 7dc4c64 on 23 Oct 2019
 History
 1 contributor
Executable File  27 lines (23 sloc)  759 Bytes
  
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

#!/usr/bin/env python3

import boto3

table_name = "orders_leaderboard"
client = boto3.client("dynamodb")

print(f"Creating {table_name} table")
response = client.create_table(
    TableName=table_name,
    KeySchema=[
        {"AttributeName": "album", "KeyType": "HASH"},
        {"AttributeName": "artist", "KeyType": "RANGE"},
    ],
    AttributeDefinitions=[
        {"AttributeName": "album", "AttributeType": "S"},
        {"AttributeName": "artist", "AttributeType": "S"},
    ],
    BillingMode="PAY_PER_REQUEST",
)
print(response)

print(f"Waiting for table {table_name}...")
waiter = client.get_waiter("table_exists")
waiter.wait(TableName=table_name)
response = client.describe_table(TableName=table_name)
print(response["Table"]["TableStatus"])
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
