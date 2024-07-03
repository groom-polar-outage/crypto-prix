<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | ~> 1.9.0 |
| <a name="requirement_helm"></a> [helm](#requirement\_helm) | 2.14.0 |
| <a name="requirement_kubernetes"></a> [kubernetes](#requirement\_kubernetes) | 2.31.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_helm"></a> [helm](#provider\_helm) | 2.14.0 |
| <a name="provider_kubernetes"></a> [kubernetes](#provider\_kubernetes) | 2.31.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [helm_release.api](https://registry.terraform.io/providers/hashicorp/helm/2.14.0/docs/resources/release) | resource |
| [helm_release.coins](https://registry.terraform.io/providers/hashicorp/helm/2.14.0/docs/resources/release) | resource |
| [helm_release.influxdb2](https://registry.terraform.io/providers/hashicorp/helm/2.14.0/docs/resources/release) | resource |
| [kubernetes_namespace.this](https://registry.terraform.io/providers/hashicorp/kubernetes/2.31.0/docs/resources/namespace) | resource |
| [kubernetes_secret.coingecko_api_key](https://registry.terraform.io/providers/hashicorp/kubernetes/2.31.0/docs/resources/secret) | resource |
| [kubernetes_secret.fastapi_users_secret](https://registry.terraform.io/providers/hashicorp/kubernetes/2.31.0/docs/resources/secret) | resource |
| [kubernetes_secret.coind_db_auth](https://registry.terraform.io/providers/hashicorp/kubernetes/2.31.0/docs/data-sources/secret) | data source |
| [kubernetes_service.coind_db](https://registry.terraform.io/providers/hashicorp/kubernetes/2.31.0/docs/data-sources/service) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_crypto_prix_conf"></a> [crypto\_prix\_conf](#input\_crypto\_prix\_conf) | input variable configs | <pre>object({<br>    kube_config = object({<br>      path    = string<br>      context = string<br>    })<br>    coingecko_api_key    = string<br>    fastapi_users_secret = string<br>    tsdb_org             = string<br>    tsdb_bucket          = string<br>    timezone             = string<br>    tsdb_bolt_path       = string<br>  })</pre> | <pre>{<br>  "coingecko_api_key": "CHANGE-ME",<br>  "fastapi_users_secret": "CHANGE-ME",<br>  "kube_config": {<br>    "context": "<rancher/docker>-desktop",<br>    "path": "~/.kube/config"<br>  },<br>  "timezone": "Europe/Prague",<br>  "tsdb_bolt_path": "~/.influxdbv2/influxd.bolt",<br>  "tsdb_bucket": "BAR",<br>  "tsdb_org": "FOO"<br>}</pre> | no |

## Outputs

No outputs.
<!-- END_TF_DOCS -->