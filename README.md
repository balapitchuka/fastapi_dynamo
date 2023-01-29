## Setup local dynamodb
> docker run -p 8000:8000 -d amazon/dynamodb-local

## Set Up DynamoDB Admin
* DynamoDB Admin to interact with it non-programmatically

Install DynamoDB Admin using npm
> npm install -g dynamodb-admin

# For Windows:
> set DYNAMO_ENDPOINT=http://localhost:8000
> dynamodb-admin

# For Mac/Linux:
> DYNAMO_ENDPOINT=http://localhost:8000 dynamodb-admin