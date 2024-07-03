# crypto-prix
Retrieves current price, daily and monthly averages.

## High level design
![high-level-design](diagrams/crypto-prix.drawio.svg)

## Requirements
- provide `terraform.tfvar` with configuration.
```terraform
crypto_prix_conf = {
  kube_config = {                       # provide config for k8s cluster
    path    = "~/.kube/config"
    context = "docker-desktop"          # rancher-desktop   
  }
  coingecko_api_key = "YOUR-API-KEY"    # Register and get token from https://www.coingecko.com/
  fastapi_users_secret = "YOUR-SECRET"  # random passphrase
  timezone = "Europe/Prague"
  tsdb_org = "FOO"                      # influxdb2 organization and bucket
  tsdb_bucket = "BAR"                   
}
```

## Example
Get port forward of coins-api service.
![port-forward](diagrams/portf.png)

### Unauthorized access
```shell
$ curl -X 'GET' \
  'http://localhost:8080/api/v1/price' \
  -H 'accept: application/json'
{"detail":"Unauthorized"}
```

### Create user
```shell
$ curl -X 'POST'   'http://localhost:8080/api/v1/register'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "email": "user12@example.com",
  "password": "foobar",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false
}'
{"id":"64ce6284-d9bf-430d-ae28-75efb1db0c98","email":"user12@example.com","is_active":true,"is_superuser":false,"is_verified":false}
```

### Get access token
```shell
$ curl -X 'POST' \
  'http://localhost:8080/api/v1/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=user12%40example.com&password=foobar&scope=&client_id=&client_secret='
{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGNlNjI4NC1kOWJmLTQzMGQtYWUyOC03NWVmYjFkYjBjOTgiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcyMDAyMzk1MX0.H4OWDmcbD4_bAfbamie8Bz4ojGooQtjJno9KOo4z3mA","token_type":"bearer"}
```

### Authorized access
```shell
$ curl -X 'GET' \
  'http://localhost:8080/api/v1/price' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGNlNjI4NC1kOWJmLTQzMGQtYWUyOC03NWVmYjFkYjBjOTgiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcyMDAyNDExOX0.DL0Tfqa8rzTpbJuS3XldSjYMV6eWTaIA9dT22e5bOn0'
{"req_time":"2024-07-03T17:28:58.024622+02:00","data":{"czk":{"last":1403313.2119,"last_updated_at":"2024-07-03T15:24:39+00:00","avg_1d":1429553.1516163375,"avg_1mo":1454832.1302047411},"usd":{"last":60278.63527,"last_updated_at":"2024-07-03T15:24:39+00:00","avg_1d":61099.515623239444,"avg_1mo":62098.05862428571}}}
```