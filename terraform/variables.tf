variable "crypto_prix_conf" {
  sensitive = true
  type = object({
    kube_config = object({
      path    = string
      context = string
    })
    coingecko_api_key = string
    fastapi_users_secret = string
    tsdb_org=string
    tsdb_bucket=string
    timezone=string
  })
  default = {
    kube_config = {
      path    = "~/.kube/config"
      context = "<rancher/docker>-desktop"
    }
    coingecko_api_key = "CHANGE-ME"
    fastapi_users_secret = "CHANGE-ME"
    timezone = "Europe/Prague"
    tsdb_org = "FOO"
    tsdb_bucket = "BAR"
  }
  description = "input variable configs"
}