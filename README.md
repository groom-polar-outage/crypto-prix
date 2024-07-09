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
{"access_token":" eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzZGEwNDNhZC05MjA4LTRiYTktOTM5ZS01Y2UyMTRiZTI2YjgiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcyMDUyMzYwN30.AFfjvQlnwTNDicH8IXEpqit-_nivISVbVisgyf1RY08A","token_type":"bearer"}
```

### Authorized access
#### Get last price
```shell
$ curl -X 'GET' \
  'http://localhost:8080/api/v1/price?coin=bitcoin&currency=czk' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzZGEwNDNhZC05MjA4LTRiYTktOTM5ZS01Y2UyMTRiZTI2YjgiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcyMDUyMzYwN30.AFfjvQlnwTNDicH8IXEpqit-_nivISVbVisgyf1RY08'
{"req_time":"2024-07-09T12:15:22.462689+02:00","data":[{"_time":"2024-07-09T10:09:27+00:00","_value":1343673.82198,"_measurement":"bitcoin","currency":"czk"}]}

```
#### Get average
```shell
$ curl -X 'GET' \
  'http://localhost:8080/api/v1/price/averages?coin=bitcoin&currency=czk&timeframe=1mo' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzZGEwNDNhZC05MjA4LTRiYTktOTM5ZS01Y2UyMTRiZTI2YjgiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcyMDUyMzYwN30.AFfjvQlnwTNDicH8IXEpqit-_nivISVbVisgyf1RY08'
{"req_time":"2024-07-09T12:15:04.739949+02:00","data":[{"_value":1441266.9462513723,"_measurement":"bitcoin","currency":"czk"}]}
```