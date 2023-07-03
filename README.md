## Test task mainhive

### Requirments:
- If you like to tackle backend processes, you can create an interesting interaction between lambdas and AWS services
- Please display your work in serverless environment (Lambda, and other serverless technologies)
- We would like to see some nicely written code
- We like to know what you did, so we would not miss anything. So please document your work, what was done and what did you try to accomplish in a separate file

### Task
Lambda handler which performs cognito creating user. The request should contain:
- email

Creation performing by POST request. 
Stack: lambda, cognito UP, API GW.

Resources: 
- app - folder with layers for executor
- lambda.py - lambda handler
- serverless.yaml - sls file
- roles.yaml - role for lambda function
- policies/ - policies for the role

### Local configuration
Deployment performing using serverless framework. For local installation please use [a link](https://gist.github.com/bretton/a82cabcc4831737b096c085441102bc5).
```
    serverless config credentials -o --provider aws --key  --secret        
    serverless plugin install -n serverless-dotenv-plugin      
    sls plugin install -n serverless-python-requirements
    serverless deploy
```

### .env

```
API_ID - API GW Id     
UP_ID - User Pool Id     
CL_ID - Client Id     
REGION - Region   
``` 
