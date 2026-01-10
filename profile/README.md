# Synkube

> **Production-ready Kubernetes infrastructure in hours, not weeks.**

Synkube is an infrastructure and DevOps automation company focused on cloud-native solutions. We build production-tested applications, platform starter kits, and deployment pipelines.

---

## 🚀 Open-Source Projects

### [Helm Charts](https://github.com/synkube/charts) [![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/synkube)](https://artifacthub.io/packages/search?repo=synkube)

| Chart | Description |
|-------|-------------|
| **[app-starter](https://artifacthub.io/packages/helm/synkube/app-starter)** | Universal chart for 99% of K8s workloads (Deployments, StatefulSets, Jobs, CronJobs) |
| **[app-extensions](https://artifacthub.io/packages/helm/synkube/app-extensions)** | Namespace-scoped resources (Secrets, ConfigMaps, RBAC, NetworkPolicies) |
| **[platform-extensions](https://artifacthub.io/packages/helm/synkube/platform-extensions)** | Cluster-scoped resources (ClusterRoles, ClusterSecretStores, Certificates) |

```bash
# Install via OCI
helm install myapp oci://ghcr.io/synkube/charts/app-starter --version 1.1.0 -f values.yaml

# Or via Helm repo
helm repo add synkube https://synkube.github.io/charts
```

---

## ☁️ Platform Deployments

### Synkube Lite (DigitalOcean)

Complete GitOps platform on DigitalOcean Kubernetes (DOKS) with ArgoCD.

| Repository | Purpose |
|------------|---------|
| **[lite-do-infra](https://github.com/synkube/lite-do-infra)** | Terraform for DOKS cluster provisioning |
| **[lite-do-argo-apps](https://github.com/synkube/lite-do-argo-apps)** | ArgoCD applications & GitOps setup |
| **[lite-do-deploy](https://github.com/synkube/lite-do-deploy)** | Helmfile-based deployments |

**Stack:** ArgoCD • External Secrets (Infisical) • cert-manager • Traefik/NGINX • Prometheus • Grafana

### GCP Deployment

Full-stack platform on Google Kubernetes Engine (GKE).

| Repository | Purpose |
|------------|---------|
| **[infra](https://github.com/synkube/infra)** | Terraform for GCP/GKE provisioning via Terraform Cloud |
| **[gke](https://github.com/synkube/gke)** | Kubernetes manifests & Helmfile deployments |

**Stack:** GKE • Workload Identity • cert-manager • ingress-nginx • Prometheus • Grafana • Teleport

---

## 🛠️ Applications

### Backend ([app](https://github.com/synkube/app))

Golang and Python applications with containerized deployments.

- **node-monitor** - Ethereum node monitoring
- **evm-indexer** - Ethereum block/transaction indexer
- **blueprint** - Application template

### Frontend ([web](https://github.com/bsgrigorov/web) • [turbo](https://github.com/synkube/turbo))

Next.js applications in Nx/Turborepo monorepos with Vercel & Cloudflare Pages deployments.

---

## 🔧 Technology Stack

| Category | Technologies |
|----------|--------------|
| **IaC** | Terraform, Terraform Cloud |
| **Cloud Providers** | AWS, GCP, DigitalOcean, Vercel |
| **Orchestration** | Kubernetes (GKE, DOKS) |
| **GitOps** | ArgoCD, Helmfile |
| **CI/CD** | GitHub Actions |
| **Secrets** | External Secrets, Infisical |
| **Networking** | Traefik, NGINX, Cloudflare |
| **Observability** | Prometheus, Grafana, Alertmanager |
| **Frontend** | Next.js, React, Tailwind CSS, SCSS, Github Pages |
| **Backend** | Golang, Python, Node.js, Express, NestJS |

---

*Infrastructure and DevOps automation for the cloud-native ecosystem.*
