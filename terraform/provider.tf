terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.31.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "2.14.0"
    }
  }

  required_version = "~> 1.9.0"
}

provider "kubernetes" {
  config_path    = var.crypto_prix_conf.kube_config.path
  config_context = var.crypto_prix_conf.kube_config.context
}

provider "helm" {
  kubernetes {
    config_path    = var.crypto_prix_conf.kube_config.path
    config_context = var.crypto_prix_conf.kube_config.context
  }
}
