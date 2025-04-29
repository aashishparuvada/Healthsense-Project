# Infrastructure Setup - Terraform

This folder contains all infrastructure-as-code (IaC) definitions used to provision the HealthSense cloud environment on **Google Cloud Platform (GCP)** using **Terraform**.

---

## 📂 Structure

```plaintext
terraform/
├── main.tf                  # Core infrastructure (GKE, CloudSQL)
├── provider.tf              # Provider configuration for GCP
├── variables.tf             # Input variables for this module
├── outputs.tf               # Output values for reference
├── terraform.tfvars         # Real input values (not versioned)
├── networking/              # VPC, Subnet, Firewall (as module)
│   ├── main.tf
│   ├── outputs.tf
│   └── variables.tf
├── storage/                 # Cloud Storage Bucket module
│   ├── main.tf
│   ├── outputs.tf
│   └── variables.tf
```

---

## ⚙️ Setup Instructions

1. Navigate to the `terraform/` folder:
   ```bash
   cd terraform/
   ```

2. Initialize Terraform:
   ```bash
   terraform init
   ```

3. Review the plan:
   ```bash
   terraform plan
   ```

4. Apply to provision infrastructure:
   ```bash
   terraform apply
   ```

---

## 🚀 Resources Provisioned

- GKE Kubernetes Cluster
- Cloud SQL Instances (PostgreSQL)
- Custom VPC and Subnet
- Firewall Rules (internal and SSH)
- Cloud Storage Bucket

---

## 🩱 Cleanup

To destroy all provisioned resources:

```bash
terraform destroy
```

---

## 📌 Notes

- Use `terraform.tfvars` to customize values (do NOT push this file to GitHub).
- Modules are kept cleanly under `networking/` and `storage/`.
- Default region is `asia-south1` (Mumbai).

---

## 🔒 Git Ignore Suggestions

Make sure the following is added to your `.gitignore`:

```
.terraform/
*.tfstate
*.tfstate.backup
terraform.tfvars
```

---