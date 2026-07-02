# Security Summary

## IAM

The EC2 instance uses an IAM Role instead of AWS access keys.

Permissions granted:

- Amazon S3 (Least Privilege)
- CloudWatch Agent
- CloudWatch Logs

---

## Security Groups

Configured inbound rules:

| Port | Purpose |
|------|----------|
| 22 | SSH |
| 80 | HTTP |

Outbound traffic uses the default allow rule.

---

## Amazon S3

- Private bucket
- File uploads performed through IAM Role
- No public access enabled

---

## Monitoring

CloudWatch monitors:

- CPU Usage
- Memory Usage
- Disk Usage
- Application Logs

CloudWatch Alarm generates an SNS email notification when CPU usage exceeds the configured threshold.

---

## Docker

Application runs inside a Docker container on EC2, providing process isolation and simplified deployment.

---

## Best Practices Followed

- IAM Least Privilege
- No AWS credentials stored in the application
- Private S3 Bucket
- Automated deployments using GitHub Actions