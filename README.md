# Cloud-Native-Monitoring

#Overview

A Python-based cloud-native monitoring application built with Flask to track CPU and memory usage. The application is containerized with Docker and deployed on an AWS EKS cluster using Kubernetes for scalability and reliability.

#Features

Real-time Monitoring: Tracks system CPU and memory usage.

Containerized Deployment: Packaged with Docker for seamless portability.

Kubernetes Orchestration: Deployed on AWS EKS for high availability and scalability.

#Tech Stack

1.Python (Flask for backend)

2.Docker (Containerization)

3.Kubernetes (Orchestration on AWS EKS)

4,AWS ECR (Container Registry for storing images)

#Setup & Deployment

Prerequisites

Docker installed

AWS CLI configured

Kubernetes (kubectl) installed

AWS EKS cluster set up

#Steps

Clone the repository

git clone https://github.com/your-repo/cloud-monitoring-app.git
cd cloud-monitoring-app

Build and push Docker image

docker build -t my-monitoring-app .
docker tag my-monitoring-app:latest <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/my-monitoring-app:latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/my-monitoring-app:latest

Deploy to Kubernetes (AWS EKS)

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

