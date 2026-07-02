# Deployment Guide

## Project Overview

This project deploys a Dockerized FastAPI application on an Amazon EC2 instance using GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD).

---

## Prerequisites

- AWS Account (Free Tier)
- Ubuntu EC2 Instance
- Docker
- GitHub Account
- Docker Hub Account

---

## Local Setup

Clone the repository.

```bash
git clone https://github.com/purvaa01/internship-assignment.git
cd internship-assignment
```

Create a virtual environment.

```bash
python3 -m venv myenv
source myenv/bin/activate
```

Install dependencies.

```bash
pip install -r app/requirements.txt
```

Run the application.

```bash
uvicorn app.main:app --host 0.0.0.0 --port 9000
```

---

## Docker

Build the Docker image.

```bash
docker build -t internship-assignment .
```

Run the container.

```bash
docker run -d -p 9000:9000 internship-assignment
```

---

## EC2 Deployment

- Launch Ubuntu EC2 instance.
- Install Docker.
- Open ports 22 and 80 in the Security Group.
- Configure IAM Role.
- Pull Docker image from Docker Hub.
- Run the Docker container.

---

## CI/CD Workflow

GitHub Actions performs the following steps automatically:

1. Checkout source code.
2. Build Docker image.
3. Push image to Docker Hub.
4. Connect to EC2 via SSH.
5. Pull latest image.
6. Replace running container.

---

## Verification

Application:

```
http://<EC2-PUBLIC-IP>/
```

Swagger UI:

```
http://<EC2-PUBLIC-IP>/docs
```