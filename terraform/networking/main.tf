resource "google_compute_network" "vpc" {
  name                    = "healthsense-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name          = "healthsense-subnet"
  ip_cidr_range = "10.0.0.0/16"
  region        = var.region
  network       = google_compute_network.vpc.id
}

resource "google_compute_firewall" "internal" {
  name    = "allow-internal-traffic"
  network = google_compute_network.vpc.name

  allow {
    protocol = "tcp"
    ports    = ["0-65535"]
  }

  source_ranges = ["10.0.0.0/16"]
}

resource "google_compute_firewall" "ssh" {
  name    = "allow-ssh-external"
  network = google_compute_network.vpc.name

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["0.0.0.0/0"]
}