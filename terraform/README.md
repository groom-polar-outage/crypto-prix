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
| [helm_release.influxdb2](https://registry.terraform.io/providers/hashicorp/helm/2.14.0/docs/resources/release) | resource |
| [kubernetes_namespace.this](https://registry.terraform.io/providers/hashicorp/kubernetes/2.31.0/docs/resources/namespace) | resource |
| [kubernetes_secret.coingecko_api_key](https://registry.terraform.io/providers/hashicorp/kubernetes/2.31.0/docs/resources/secret) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_crypto_prix_conf"></a> [crypto\_prix\_conf](#input\_crypto\_prix\_conf) | configs | <pre>object({<br>    kube_config = object({<br>      path = string<br>      context = string<br>    })<br>    coingecko_api_key = string<br>  })</pre> | <pre>{<br>  "coingecko_api_key": "CHANGE-ME",<br>  "kube_config": {<br>    "context": "rancher-desktop",<br>    "path": "./kube/config"<br>  }<br>}</pre> | no |

## Outputs

No outputs.
<!-- END_TF_DOCS -->