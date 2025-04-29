output "gke_cluster_name" {
  value = google_container_cluster.primary.name
}

output "healthsense_db_instance_name" {
  value = google_sql_database_instance.healthsense.name
}

output "airflow_db_instance_name" {
  value = google_sql_database_instance.airflow_metadata.name
}