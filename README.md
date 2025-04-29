# HealthSense - Health Data Analytics Platform

An end-to-end health data analytics and predictive insights platform built on **Google Cloud Platform (GCP)** using **Python**, **PostgreSQL**, **Docker**, **Kubernetes**, **Airflow**, **Terraform**, and **Prometheus/Grafana** for monitoring.

---

## 🚀 Project Architecture

```
Data Sources (MIMIC-III, Public Health APIs)
   ↓
Apache Airflow (ETL Pipelines)
   ↓
Cloud Storage → Cloud SQL (PostgreSQL)
   ↓
Machine Learning Models (TensorFlow, XGBoost)
   ↓
FastAPI Microservices (APIs)
   ↓
GKE Cluster (Kubernetes)
   ↓
Monitoring (Prometheus + Grafana)
```

---

## 🛠️ Tech Stack

| Layer               | Technology |
|---------------------|------------|
| Cloud Provider      | Google Cloud Platform (GCP) |
| Infrastructure as Code | Terraform |
| Data Engineering    | Apache Airflow |
| Data Storage        | Cloud SQL (PostgreSQL), Google Cloud Storage |
| Machine Learning    | TensorFlow, XGBoost |
| Backend APIs        | FastAPI (Python) |
| Containers          | Docker |
| Container Orchestration | GKE (Google Kubernetes Engine) |
| Monitoring          | Prometheus, Grafana |

---

## 🔂 Project Structure

```plaintext
healthsense-project/
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── terraform.tfvars (NOT pushed to GitHub)
│   ├── networking/
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   └── variables.tf
│   ├── storage/
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   └── variables.tf
├── api/
│   └── (FastAPI application code)
├── etl/
│   └── (Airflow DAGs and ETL scripts)
├── docker/
│   └── (Dockerfiles for services)
├── kubernetes/
│   └── (Kubernetes YAMLs for deployment and services)
├── ml-models/
│   └── (Machine learning training and inference code)
├── README.md
└── .gitignore
```

---

## 🌐 Infrastructure Provisioning (Terraform)

1. Navigate to terraform directory:
    ```bash
    cd terraform/
    ```

2. Initialize Terraform:
    ```bash
    terraform init
    ```

3. Plan resources:
    ```bash
    terraform plan
    ```

4. Apply resources:
    ```bash
    terraform apply
    ```

- Provisioned resources:
  - GKE Kubernetes Cluster
  - Cloud SQL Databases
  - VPC Network
  - Subnet and Firewall rules
  - Storage Buckets

---

## 🩱 Microservices Deployment (Kubernetes)

- APIs, ETL, and ML model services are Dockerized.
- Deployed to GKE using Kubernetes manifests:
    - `Deployment`
    - `Service`
    - `ConfigMap`
    - `Ingress` (Optional: for HTTPS / domain)
- Managed using `kubectl` and Kubernetes dashboard.

---

## 📊 Monitoring

- Prometheus deployed inside GKE.
- Grafana used for real-time dashboard and alerts.

Monitoring Metrics:
- Pod status
- API response time
- Database connection health
- ETL pipeline runs

---

## 📚 How to Use

1. Build Docker images for API/ML/ETL components.
2. Push Docker images to GCP Artifact Registry.
3. Deploy Kubernetes manifests (`kubectl apply -f`).
4. Expose APIs via Kubernetes services.
5. Access dashboards (Streamlit, Grafana).
6. Run Airflow DAGs to trigger ETL pipelines.

---

## 🩱 Resource Cleanup

After project completion:

```bash
cd terraform/
terraform destroy
```
- This command will destroy all cloud resources (GKE, SQL, VPC, Buckets) to avoid unnecessary costs.

---

## 📜 Best Practices Followed

- Clean separation of infrastructure and application code
- Secure resource access with IAM roles
- Git ignored sensitive files (`terraform.tfvars`, `.terraform/`, `.env`)
- Modularized Terraform setup
- Regional resource deployment (Asia-South1 - Mumbai)

---

## 📢 Future Enhancements

- Implement CI/CD pipelines (Cloud Build, GitHub Actions)
- Advanced ML model serving (TF Serving / TorchServe)
- Autoscaling Kubernetes workloads
- Role-based API Authentication
- ETL pipeline versioning

---

## 🙌 Acknowledgments

- GCP Free Tier Program
- Open Datasets (MIMIC-III, WHO Global Health data)
- Terraform by HashiCorp
- Kubernetes and Docker open-source community

---

## 📬 Contact

Feel free to reach out for collaborations or queries!

- GitHub: [aashishparuvada](https://github.com/aashishparuvada)
- LinkedIn: [Aashish Paruvada](https://www.linkedin.com/in/aashishparuvada)

---