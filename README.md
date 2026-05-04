# Claims Status API – CI/CD Pipeline Project

## Overview

This project demonstrates a **production-style CI/CD pipeline** using GitHub Actions, Docker, and AWS EC2.

The pipeline automates:
- Code validation (lint + tests)
- Docker image build and publishing
- Deployment to a staging environment
- Production approval workflow
- Health checks and rollback strategy

---

## Architecture

![Architecture Diagram](architecture.png)

Key Components:
- GitHub Actions (CI/CD)
- GitHub Container Registry (GHCR)
- Dockerized Flask Application
- AWS EC2 for deployment

---

## CI/CD Pipeline Flow

### CI Pipeline (Pull Requests)
- Checkout code
- Install dependencies
- Run lint checks (flake8)
- Execute unit tests (pytest)
- Build Docker image

### CD Pipeline (Main Branch)
- Build and tag Docker image
- Push image to GHCR
- Deploy to EC2 instance
- Run health check validation

### Production Deployment
- Manual approval required
- Controlled release mechanism

---

## Technologies Used

- Python (Flask)
- Docker
- GitHub Actions
- GitHub Container Registry (GHCR)
- AWS EC2
- Linux (Amazon Linux)

---

## Deployment Process

1. Developer pushes code
2. CI pipeline validates changes
3. Code merged into main branch
4. Docker image built and pushed
5. CD pipeline deploys to EC2
6. Health check validates deployment

---

## Troubleshooting Scenarios (Real-World Practice)

This project includes built-in failure scenarios:

### 1. Failed Unit Tests
- Diagnose test failures via logs
- Fix and re-run pipeline

### 2. Docker Build Failure
- Debug Dockerfile issues
- Validate build context

### 3. Deployment Failure
- Inspect container logs
- Validate port mappings

### 4. Health Check Failure
- Investigate application errors
- Perform rollback

### 5. Secrets Misconfiguration
- Debug authentication issues
- Validate GitHub secrets

---

## Key Commands (Production Support Style)

```bash
docker ps
docker logs claims-api
docker inspect claims-api
curl http://localhost:5000/health
systemctl status docker
df -h