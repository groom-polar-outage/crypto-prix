from json import loads
from influxdb_client import InfluxDBClient
from loguru import logger

from app.config import CONFIG


def _query_storage(query: str, columns: list[str]):
    client = InfluxDBClient(
        url=CONFIG.TSDB_URL, token=CONFIG.TSDB_TOKEN, org=CONFIG.TSDB_ORG
    )
    query_api = client.query_api()
    return query_api.query(query=query, org=CONFIG.TSDB_ORG).to_json(columns=columns)


def get_last_data(coin: str, currency: str):
    logger.info(f"Start fetching last data for {coin} in {currency}...")

    query = f"""from(bucket: "{CONFIG.TSDB_BUCKET}") \
    |> range(start: -15m, stop: now()) \
    |> filter(fn: (r) => r._measurement == "{coin}" and r.currency == "{currency}") \
    |> tail(n: 1)"""

    tsdb_resp = _query_storage(query, ["_measurement", "currency", "_time", "_value"])

    return loads(tsdb_resp)


def get_average_data(coin: str, currency: str, timeframe: str):
    logger.info(
        f"Start fetching average data for {coin} in {currency} for last {timeframe}..."
    )

    query = f"""from(bucket: "{CONFIG.TSDB_BUCKET}") \
    |> range(start: -{timeframe}, stop: now()) \
    |> filter(fn: (r) => r._measurement == "{coin}" and r.currency == "{currency}") \
    |> mean()"""

    tsdb_resp = _query_storage(query, ["_measurement", "currency", "_value"])

    return loads(tsdb_resp)
