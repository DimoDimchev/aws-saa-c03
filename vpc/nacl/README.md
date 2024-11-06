## Overview
NACL's are a stateless virtual firewall for compute within a VPC. They operate at the subnet level
- you can set both **DENY** & **ALLOW** rules
- *each VPC has a default NACL*
- each NACL has inbound rules and outbound rules
- *a subnet can belong to only one NACL*
- **rule numbers should be increments of 10 or 100**

## Examples using the AWS CLI

#### Create NACL
```sh
aws ec2 create-network-acl --vpc-id <id>
```

#### Add entry
```sh
aws ec2 create-network-acl-entry \
--network-acl-id <id> \
--ingress \
--rule-number 90 \
--protocol -1 \
--port-range From=<range-start>,To=<range-end> \
--cidr-block <block> \
--rule-action deny
```