## Overview
Bucket policies define permissions for *an entire S3 bucket* using JSON-based policies.
- **Bucket policies should be used over ACL's since they are much more flexible**
- **Bucket policies look like [this](./policy.json)**

## Example using the AWS CLI
```sh
aws s3api put-bucket-policy \
--bucket <existing-bucket-name> \
--policy file://<path-to-policy-file>
```