variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  default     = "asia-south1"   # Mumbai
}

variable "zone" {
  description = "GCP zone"
  default     = "asia-south1-c" # Mumbai Zone C
}

variable "gke_cluster_name" {
  description = "Name of Kubernetes cluster"
  default     = "healthsense-gke"
}

variable "db_instance_name" {
  description = "Name of Cloud SQL DB for HealthSense"
  default     = "healthsense-db"
}

variable "airflow_db_instance_name" {
  description = "Name of Cloud SQL DB for Airflow Metadata"
  default     = "airflow-metadata-db"
}