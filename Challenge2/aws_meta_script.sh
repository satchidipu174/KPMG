#!/bin/bash
aws ec2 describe-instances --query "Reservations[*].Instances[*].{PublicIP:PublicIpAddress,PrivateIP:PrivateIpAddress,InstanceID:InstanceId,ImageID:ImageId,KeyName:KeyName,InstanceType:InstanceType,Name:Tags[?Key=='Name']|[0].Value,Status:State.Name}" --output json
