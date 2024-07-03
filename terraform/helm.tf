resource "helm_release" "influxdb2" {
  repository = "https://helm.influxdata.com"
  chart      = "influxdb2"
  version    = "2.1.2"

  name        = "coin-db"
  description = "Install influxdb2 used for coin time series data."

  namespace = kubernetes_namespace.this.id

  atomic       = true
  reset_values = true
  reuse_values = true

  values = [templatefile("${path.root}/templates/influxdb.tftpl", {
    TSDB_ORG = var.crypto_prix_conf.tsdb_org
    TSDB_BUCKET = var.crypto_prix_conf.tsdb_bucket
    RETENTION = "52w"
    PERSISTENCE = false
  } )]
}

data "kubernetes_secret" "coind_db_auth" {
  metadata {
    namespace = kubernetes_namespace.this.id
    name = "coin-db-influxdb2-auth"
    labels = {
      "app.kubernetes.io/instance" = helm_release.influxdb2.id
      "app.kubernetes.io/name" = helm_release.influxdb2.chart
    }
  }
  binary_data = {
    admin-token=""
  }
}

data "kubernetes_service" "coind_db" {
  metadata {
    namespace = kubernetes_namespace.this.id
    name = "coin-db-influxdb2"
    labels = {
      "app.kubernetes.io/instance" = helm_release.influxdb2.id
      "app.kubernetes.io/name" = helm_release.influxdb2.chart
    }
  }
}

resource "helm_release" "coins" {
  chart = "${path.root}/helm-charts/crypto-prix-coins"
  name  = "coins-job"
  description = "Install cronjob used to fetch coin data."

  namespace = kubernetes_namespace.this.id

  atomic = true
  reset_values = true
  reuse_values = true

  values = [templatefile("${path.root}/templates/coins-db.tftpl", {
    TAG="0.1.2"
    CRON="*/5 * * * *"
    TIMEZONE=var.crypto_prix_conf.timezone
    TSDB_ORG=var.crypto_prix_conf.tsdb_org
    TSDB_BUCKET=var.crypto_prix_conf.tsdb_bucket
    TSDB_URL=data.kubernetes_service.coind_db.metadata[0].name
    TSDB_SECRET_NAME=data.kubernetes_secret.coind_db_auth.metadata[0].name
    TSDB_SECRET_KEY="admin-token"
    CG_SECRET_NAME=kubernetes_secret.coingecko_api_key.metadata[0].name
    CG_SECRET_KEY="api-key"
  })]

}

resource "helm_release" "api" {
  chart = "${path.root}/helm-charts/coins-api"
  name  = "coins-api"
  description = "API to get coin price data."

  namespace = kubernetes_namespace.this.id

  atomic = true
  reset_values = true
  reuse_values = true

  values = [templatefile("${path.root}/templates/coins-api.tftpl", {
    TAG="0.2.2"
    TIMEZONE=var.crypto_prix_conf.timezone
    TSDB_ORG=var.crypto_prix_conf.tsdb_org
    TSDB_BUCKET=var.crypto_prix_conf.tsdb_bucket
    TSDB_URL=data.kubernetes_service.coind_db.metadata[0].name
    TSDB_SECRET_NAME=data.kubernetes_secret.coind_db_auth.metadata[0].name
    TSDB_SECRET_KEY="admin-token"
    FASTAPI_SECRET_NAME=kubernetes_secret.fastapi_users_secret.metadata[0].name
    FASTAPI_SECRET_KEY="secret"
  })]
}
