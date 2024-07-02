locals {
  namespace = "crypto-prix"
}

resource "kubernetes_namespace" "this" {
  metadata {
    name = local.namespace
    labels = {
      "kubernetes.io/metadata.name" = local.namespace
      name                          = local.namespace
    }
  }
}

resource "kubernetes_secret" "coingecko_api_key" {
  metadata {
    name      = "coingecko-api-key"
    namespace = kubernetes_namespace.this.id
  }

  data = {
    api-key = var.crypto_prix_conf.coingecko_api_key
  }
}