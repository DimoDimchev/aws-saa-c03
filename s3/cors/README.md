## Overview
CORS allows a server to indicate *any* other origins(domain, scheme or port) than its own from which a browser should permit loading of resources
- **CORS restricts which websites may access data to be loaded onto its page**
- **S3 allows you to set CORS configuration to a S3 bucket with static website hosting so different origins can perform HTTP requests from your S3 static website**
    - the config file can be either XML or JSON
    - config files look like [this](./config.json)

## Example using the AWS CLI
```sh
aws s3api put-bucket-cors \
--bucket <existing-bucket-name> \
--cors-configuration file://<path-to-config-file>
```