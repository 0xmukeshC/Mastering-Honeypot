# AWS Honeypot Setup

## Create a new AWS account

If you don't have an AWS account, create one by signing up on the AWS website.

## Sign-in to your AWS account

Visit the AWS website and sign in to your AWS account using your credentials.

## Create and Configure S3 Bucket

### Navigate to S3 Service
- Search for S3 service in the AWS Management Console's search bar and navigate to it.

### Create a New Bucket
- Click on the "Create bucket" button.
- Choose a unique name and region for the bucket. For example, "cyberveer-bucket" in the Asia Pacific region.

### Configure Object Ownership
- By default, ACLs (Access Control Lists) are disabled. Consider enabling ACLs for object ownership configuration.

### Allow Public Access
- Uncheck the "Block all public access" option to allow public access to the bucket.

### Acknowledge Prompt and Create Bucket
- Keep the other settings as default and click on "Create Bucket."

## Configure S3 Bucket

### Navigate to Bucket Permissions
- Open the created bucket and navigate to the permissions tab.

### Edit Access Control List (ACL)
- Access Control Lists (ACLs) specify permissions for objects. Edit the ACL to grant appropriate access.

### Populate Bucket with Fake Data
- Click "Upload" and choose the file you wish to upload. Ensure no classified data is uploaded.

### Update Predefined ACLs
- Change the Predefined ACLs to "Grant public-read access."

### Note ARN Number
- Amazon Resource Names (ARNs) uniquely identify AWS resources. Note down the ARN number for future reference.

### Access Uploaded File
- Visit the S3 URI to verify public access to the uploaded file.

## Configure Logging with AWS CloudTrail

### Enable CloudTrail
- Search for AWS CloudTrail service and navigate to it.
- Click on "Create trail" and configure logging settings.

### Choose Log Events
- Uncheck unnecessary log events and select "Data events" for S3.

### Configure Custom Log Selector
- Specify conditions to log specific data related to S3 bucket access.

### Review and Create Trail
- Review the configuration and create the CloudTrail trail.

## Attack Scenario

- When malicious adversaries visit the S3 bucket resource link, access events get logged.

## Logs Monitoring and Analysis with CloudWatch

### Navigate to CloudWatch
- Click on "Logs" in the CloudWatch window to view log groups.

### Access CloudTrail Logs
- View the most recent CloudTrail log groups to obtain log streams.

### Analyze Log Streams
- Analyze event logs of unauthorized access to the S3 bucket.

