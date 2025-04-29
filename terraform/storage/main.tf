resource "google_storage_bucket" "bucket" {
  name          = "healthsense-platform-bucket"
  location      = var.region
  force_destroy = true
}