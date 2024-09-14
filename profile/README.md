![infra](../assets/synkube-infra.drawio.svg)

# Synkube Infrastructure and Applications Documentation

## Overview

Synkube is a comprehensive full-stack platform that integrates infrastructure, DevOps, backend, and frontend development. It emphasizes built-in security, monitoring, authentication, and an enhanced developer experience. The platform automates Docker image packaging, Helm chart management, and deployments through GitHub Actions and Vercel workflows. Designed for agility, it enables rapid deployment of new services, frontends, clusters, and projects. The entire environment operates cost-effectively, utilizing free trial accounts and free tiers where possible, with an estimated monthly cost of approximately **$100**.

---

## Table of Contents

- [Synkube Infrastructure and Applications Documentation](#synkube-infrastructure-and-applications-documentation)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [GitHub](#github)
    - [Teams](#teams)
    - [Repositories](#repositories)
    - [CI/CD Pipelines](#cicd-pipelines)
  - [Infrastructure](#infrastructure)
    - [Terraform Cloud](#terraform-cloud)
      - [Auth Workspace](#auth-workspace)
      - [Base Workspace](#base-workspace)
  - [Google Cloud Platform (GCP)](#google-cloud-platform-gcp)
    - [GCP Project Base](#gcp-project-base)
    - [GKE Cluster](#gke-cluster)
  - [Docker and Kubernetes](#docker-and-kubernetes)
    - [Kubernetes Components](#kubernetes-components)
    - [Helm Deployments with Helmfile](#helm-deployments-with-helmfile)
  - [Backend Services](#backend-services)
    - [App Repository](#app-repository)
  - [Web Services](#web-services)
    - [Web Repository](#web-repository)
    - [Frontend Applications](#frontend-applications)
    - [Backend Applications](#backend-applications)
  - [Vercel and Cloudflare](#vercel-and-cloudflare)
    - [Vercel](#vercel)
    - [Cloudflare Pages](#cloudflare-pages)
    - [DNS Management](#dns-management)
  - [Conclusion](#conclusion)

---

## GitHub

Synkube's code repositories are hosted on GitHub, utilizing teams for access control and CI/CD pipelines for automated deployments.

### Teams

- **kube-admin**: Administrative access to all repositories and settings.
- **kube-editor**: Write access for development and deployment tasks.
- **kube-viewer**: Read-only access for code review and collaboration.

### Repositories

- **[`synkube/infra`](https://github.com/synkube/infra)**: Infrastructure repository containing Terraform configurations.
- **[`synkube/gke`](https://github.com/synkube/gke)**: Kubernetes deployment repository for cluster configurations.
- **[`synkube/app`](https://github.com/synkube/app)**: Backend application repository containing Golang and Python services.
- **[`bsgrigorov/web`](https://github.com/bsgrigorov/web)**: Full-stack application repository with Node.js (Express, NestJS) backend and React, Next.js frontend.

### CI/CD Pipelines

- **GitHub Actions**: Automates building, testing, and deploying applications and infrastructure changes.
  - **Infrastructure**: Terraform configurations are validated and applied through GitHub Actions workflows.
  - **Applications**: Docker images are built and pushed to container registries, followed by deployment to Kubernetes.
- **Vercel Workflows**: Manages frontend deployments for React and Next.js applications hosted on Vercel.

---

## Infrastructure

Synkube utilizes Infrastructure as Code (IaC) with Terraform, managed through Terraform Cloud, to provision and manage resources on GCP.

### Terraform Cloud

Provides centralized state management and execution environments for consistent infrastructure provisioning.

#### Auth Workspace

- **Purpose**: Manages authentication resources.
- Execution environment is local and state is stored in Terraform Cloud.
- **Components**:
  - **Provisioner Service Account (SA)**: Allows Terraform Cloud to securely provision GCP resources using the Base workspace.
  - **Workload Identity Provider and Pool**: Enables OIDC authentication between Terraform Cloud and GCP for kubernetes provisioning.

#### Base Workspace

- **Purpose**: Manages core infrastructure components.
- Terraform Cloud is used for state management and execution.
- **Components**:
  - **GKE Cluster**: Deploys and manages the Kubernetes cluster named `base`.
  - **Service Accounts**: Grants necessary permissions to applications and services.
  - **Workload Identity Provider and Pool for GitHub Actions**: Allows GitHub Actions workflows to authenticate securely with GCP, voiding the use of long-lived credentials.
  - **Bastion Host** and **Connect Gateway**: Provide secure access to the private GKE cluster.
  - **Cloudflare Token**: Stored as a Kubernetes secret for secure integration with Cloudflare services.

---

## Google Cloud Platform (GCP)

Synkube's infrastructure is primarily hosted on GCP, leveraging services for compute, storage, and networking.

### GCP Project Base

- **Organization**: `synkube.com`
- **Project**: `base`

### GKE Cluster

- **Name**: `base`
- **Description**: Hosts Synkube's applications and services within a private, secure environment.
- **Features**:
  - Private cluster setup with restricted access.
  - Integrated with Cloud Monitoring and Logging for observability.
  - Autoscaling enabled to optimize resource usage.

---

## Docker and Kubernetes

Applications are containerized using Docker and orchestrated with Kubernetes, providing scalability and resilience.

Repository: [`synkube/gke`](https://github.com/synkube/gke)

### Kubernetes Components

- **cert-manager**: Automates TLS certificate management.
- **external-dns**: Updates DNS records via the Cloudflare API.
  - **Cloudflare Token**: Stored in a Kubernetes secret for secure interactions with Cloudflare.
- **ingress-nginx**: Manages external access to services.
- **volume-snapshotter**: Handles backup and restore operations for persistent volumes.
- **keel**: Automates Kubernetes deployment updates.
- **Monitoring Tools**:
  - **Prometheus**: Metrics collection.
  - **Grafana**: Metrics visualization.
  - **Alertmanager**: Alert routing and management.
- **Security Tools**:
  - **Teleport**: Ensures secure access to Kubernetes resources for developers and for CI/CD workflows.


### Helm Deployments with Helmfile

- **Helm Charts**: Package Kubernetes manifests for application deployment.
- **Helmfile**: Manages multiple Helm charts, simplifying deployments and upgrades.
- **Automated Deployments**: CI/CD pipelines trigger Helm deployments upon code changes.

---

## Backend Services

Backend applications are developed in Golang and Python, focusing on performance and efficiency.

### App Repository

- **Repository**: [`synkube/app`](https://github.com/synkube/app)
- **Technologies**:
  - **Golang**: High-performance APIs and services.
  - **Python**: Data processing and automation tasks.
- **Deployment**:
  - Packaged into Docker images.
  - Deployed to the Kubernetes cluster using Helm charts managed by Helmfile.
- **CI/CD**:
  - Automated builds and tests via GitHub Actions.
  - Continuous deployment to the GKE cluster upon successful builds.

---

## Web Services

The [`bsgrigorov/web`](https://github.com/bsgrigorov/web) repository contains full-stack applications with both frontend and backend components.

### Web Repository

- **Repository**: [`bsgrigorov/web`](https://github.com/bsgrigorov/web)
- **Technologies**:
  - **Frontend**: React, Next.js.
  - **Backend**: Node.js with Express and NestJS frameworks.

### Frontend Applications

- **Deployment Platforms**:
  - **Vercel**: Hosts dynamic frontend applications build with NextJS.
  - **Cloudflare Pages**: Serves static website exports for performance optimization.
  - **Kubernetes Cluster**: Deploys containerized frontend applications.
- **Features**:
  - Server-side rendering and static site generation with Next.js.
  - Automated deployments through Vercel and GitHub Actions.

### Backend Applications

- **Technologies**: Node.js applications using Express and NestJS frameworks.
- **Deployment**:
  - Containerized with Docker. Optimized docker images for size and speed of deployment.
  - Deployed to the Kubernetes cluster via Helm charts.
- **CI/CD**:
  - GitHub Actions automate the build and deployment processes.

---

## Vercel and Cloudflare

### Vercel

- **Purpose**: Provides a platform for frontend developers to host and deploy web applications effortlessly.
- **Usage**:
  - Hosts Next.js applications.
  - Integrates with GitHub for seamless deployments upon code changes.

### Cloudflare Pages

- **Purpose**: Offers a global platform for deploying static websites directly from the GitHub repository.
- **Usage**:
  - Hosts static exports of frontend applications.
  - Provides fast and secure content delivery.

### DNS Management

- **Cloudflare DNS**:
  - Manages domain name resolution for `synkube.com`.
  - Provides standard protection services, including DDoS mitigation.
- **Integration with Kubernetes**:
  - `external-dns` updates DNS records automatically via the Cloudflare API.
  - The Cloudflare API token is securely stored in a Kubernetes secret.

---

## Conclusion

Synkube presents a robust full-stack solution that integrates infrastructure, DevOps, backend, and frontend development. By prioritizing security, automation, and developer experience, the platform streamlines the process of building and deploying applications. Key technologies and practices include:

- **GitHub**: Centralized code management with collaborative teams and automated CI/CD pipelines.
- **Infrastructure as Code with Terraform Cloud**: For consistent and repeatable provisioning, utilizing long-lived credentials.
- **GCP and GKE**: Scalable and secure hosting of applications and services.
- **Docker and Kubernetes**: Containerization and orchestration for efficient resource utilization.
- **Kubernetes Components**: Essential tools for management, security, and monitoring, including cert-manager, external-dns, ingress-nginx, volume-snapshotter, keel, Prometheus, Grafana, Alertmanager, and Teleport.
- **Helm and Helmfile**: Simplified management of Kubernetes deployments.
- **Backend Services**: High-performance applications in Golang, Python, and Node.js.
- **Frontend Services**: Dynamic and static web applications using React and Next.js, deployed via Vercel and Cloudflare Pages.
- **Automation**: GitHub Actions and Vercel workflows for continuous integration and deployment.
- **Cost Efficiency**: Utilization of free trial accounts and free tiers to maintain operational costs around <$100 per month.

**Benefits of the Synkube Platform**:

- **Rapid Deployment**: Easily spin up new services and applications.
- **Scalability**: Infrastructure designed to grow with demand.
- **Security**: Integrated authentication, monitoring, and security.
- **Developer Experience**: Streamlined workflows and automation enhance productivity.

---

**Note**: For detailed configurations, deployment instructions, and operational procedures, please refer to the respective repositories and internal documentation.
