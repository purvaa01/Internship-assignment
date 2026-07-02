# AWS DevOps Internship Assignment

An end-to-end AWS DevOps project demonstrating the deployment of a containerized FastAPI application on Amazon EC2 using Docker, automated CI/CD with GitHub Actions, Amazon S3 integration, CloudWatch monitoring, and performance testing using k6.

---

## Project Overview

This project demonstrates a complete DevOps workflow using AWS Free Tier services. The application is containerized using Docker, automatically deployed to an EC2 instance through GitHub Actions, monitored using Amazon CloudWatch, and performance-tested using k6.

---

## Features

- Deploy a FastAPI application on AWS EC2
- Containerize the application using Docker
- Automated CI/CD pipeline using GitHub Actions
- Automatic deployment to EC2
- Upload files to Amazon S3
- IAM Role with Least Privilege access
- CloudWatch Monitoring
- CloudWatch Dashboard
- CloudWatch Alarm with SNS Email Notification
- CloudWatch Log Collection
- Load Testing using k6
- Performance Analysis

---

## Architecture

![Architecture Diagram](architecture/architecture-diagram.png)

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Framework | FastAPI |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud Platform | AWS Free Tier |
| Compute | Amazon EC2 |
| Storage | Amazon S3 |
| Identity | IAM |
| Monitoring | Amazon CloudWatch |
| Notifications | Amazon SNS |
| Load Testing | k6 |
| Operating System | Ubuntu |

---

## AWS Services Used

- Amazon EC2
- Amazon S3
- IAM
- Amazon CloudWatch
- Amazon SNS

---

## Project Structure

```text
internship-assignment/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── app/
│   ├── main.py
│   └── requirements.txt
│
├── docs/
│   ├── Deployment_Guide.md
│   ├── Security_summary.md
│   ├── Load_test_report.md
│   └── Final_report.md
│
├── load-testing/
│   └── load-test.js
│
├── monitoring/
│   └── amazon-cloudwatch-agent.json
│
├── screenshots/
│
├── architecture/
│   └── architecture-diagram.png
│
├── Dockerfile
├── README.md
├── .gitignore
└── .dockerignore
```

---

## CI/CD Pipeline

The deployment pipeline is automated using **GitHub Actions**.

### Pipeline Workflow

1. Checkout source code
2. Build Docker image
3. Push Docker image to Docker Hub
4. Connect to EC2 via SSH
5. Pull latest Docker image
6. Stop existing container
7. Deploy updated container

---

## Monitoring

CloudWatch is configured to collect:

- CPU Usage
- Memory Usage
- Disk Usage
- Application Logs

CloudWatch Dashboard provides real-time monitoring.

CloudWatch Alarm triggers an SNS email notification when CPU utilization exceeds the configured threshold.

---

## Load Testing

Tool Used:

- k6

Configuration:

- Virtual Users: 20
- Duration: 1 minute

### Results

| Metric | Result |
|---------|--------|
| Total Requests | 976 |
| Successful Requests | 976 |
| Failed Requests | 0 |
| Error Rate | 0% |
| Average Response Time | 238.47 ms |
| Throughput | 15.98 requests/sec |
| 95th Percentile Response Time | 273.70 ms |

---

## Performance Analysis

The application successfully handled concurrent traffic generated during load testing.

Observations:

- Zero failed requests
- Stable response time
- Stable CPU utilization
- Stable memory usage

Possible Optimizations:

- Application Load Balancer
- Auto Scaling
- Response Caching
- Application Performance Tuning

---

## Security

- IAM Role with Least Privilege
- Private S3 Bucket
- EC2 Security Groups
- Dockerized Application
- CloudWatch Monitoring
- SNS Alert Notifications

---

## Screenshots

Project screenshots are available in the **screenshots/** directory.

They include:

- Application Deployment
- GitHub Actions Pipeline
- Amazon S3 Upload
- CloudWatch Dashboard
- CloudWatch Alarm
- CloudWatch Logs
- k6 Load Testing

---

## Documentation

Detailed documentation is available in the **docs/** folder.

- Deployment Guide
- Security Summary
- Load Test Report
- Final Project Report

---

## Future Improvements

- HTTPS using AWS Certificate Manager and Load Balancer
- API Gateway Integration (where applicable)
- Auto Scaling
- Infrastructure as Code using Terraform
- Kubernetes Deployment

---

## Author

**Purva Wankhede**

GitHub: https://github.com/<your-username>

---

## License

This project was developed as part of an AWS DevOps Internship Assignment for learning purposes.