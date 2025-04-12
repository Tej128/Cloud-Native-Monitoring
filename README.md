# 📊 Cloud-Native Monitoring App (Flask + Docker + AWS EKS)

This project demonstrates a cloud-native monitoring application built with **Flask**, containerized using **Docker**, and deployed on **AWS EKS** using **Kubernetes**. It tracks system metrics like CPU and memory in real time.

---

## 🚀 Features

- 📈 **Real-time Monitoring**: View CPU and memory usage instantly
- 🐳 **Containerized**: Dockerized for portable, repeatable deployments
- ☁️ **Cloud-Native**: Runs on AWS EKS with Kubernetes orchestration
- 📦 **ECR Integration**: Uses AWS Elastic Container Registry for image storage

---

## 🔧 Tech Stack

- **Python (Flask)**
- **Docker**
- **Kubernetes** on **AWS EKS**
- **AWS ECR**
- Optional: Prometheus/Grafana (if added later)

---

## ⚙️ Getting Started

### 🔑 Prerequisites

- Docker installed
- AWS CLI configured
- `kubectl` installed and connected to an EKS cluster
- AWS ECR repository created

### 🛠️ Steps

```bash
# 1. Clone the repository
git clone https://github.com/Tej128/Cloud-Native-Monitoring.git
cd Cloud-Native-Monitoring

# 2. Build and tag Docker image
docker build -t cloud-monitoring-app .

# 3. Push to AWS ECR
aws ecr get-login-password | docker login --username AWS --password-stdin <your_ecr_repo_url>
docker tag cloud-monitoring-app <your_ecr_repo_url>
docker push <your_ecr_repo_url>

# 4. Deploy to EKS using kubectl
kubectl apply -f k8s/


