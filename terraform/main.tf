# GKE Cluster
resource "google_container_cluster" "primary" {
  name     = var.gke_cluster_name
  location = var.region
  remove_default_node_pool = true
  initial_node_count = 1
}

resource "google_container_node_pool" "primary_nodes" {
  name    = "primary-node-pool"
  location = var.region
  cluster  = google_container_cluster.primary.name

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 30
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
    ]
  }

  initial_node_count = 2
}

# CloudSQL Databases
resource "google_sql_database_instance" "healthsense" {
  name             = var.db_instance_name
  database_version = "POSTGRES_14"
  region           = var.region

  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_database_instance" "airflow_metadata" {
  name             = var.airflow_db_instance_name
  database_version = "POSTGRES_14"
  region           = var.region

  settings {
    tier = "db-f1-micro"
  }
}

# Import networking module
module "networking" {
  source = "./networking"
  region = var.region
}

# Import storage module
module "storage" {
  source = "./storage"
  region = var.region
}