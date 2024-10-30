## Overview
ACL's are used to grant *basic read/write permissions* to other AWS accounts.
- **ACL's are a legacy feature!**
- you **can’t** grant permissions to users in your accounts
- you **can’t** grant conditional permissions
- you **can’t** explicitly deny permissions
- ACL's must be enabled from Object Ownership in order to be able to edit them

## Example using the AWS CLI
**Before running the following you have to setup an access control policy like the one [here](policy.xml). If you don't provide a policy the ACL will default to a private ACL meaning only the owner will have access.**

*You will need the canonical user ID when configuring the policy. That can be found in the "Security credentials" page in the AWS console*
```sh
aws s3api put-bucket-acl \
--bucket <existing-bucket-name> \
--access-control-policy file://<path-to-policy-file>
```