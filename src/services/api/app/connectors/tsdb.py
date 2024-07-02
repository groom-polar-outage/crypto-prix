from json import loads
from influxdb_client import InfluxDBClient
from loguru import logger

from app.config import CONFIG


_query_last = f"""from(bucket: "{CONFIG.TSDB_BUCKET}") |> range(start: -15m, stop: now()) |> tail(n: 1)"""
_query_avg_1d = f"""from(bucket: "{CONFIG.TSDB_BUCKET}") |> range(start: -1d, stop: now()) |> mean() |> group()"""
_query_avg_1mo = f"""from(bucket: "{CONFIG.TSDB_BUCKET}") |> range(start: -1mo, stop: now()) |> mean() |> group()"""


def _query_storage(query):
    client = InfluxDBClient(url=CONFIG.TSDB_URL, token=CONFIG.TSDB_TOKEN, org=CONFIG.TSDB_ORG)
    query_api = client.query_api()
    return query_api.query(query=query, org=CONFIG.TSDB_ORG).to_json(columns=['currency','_value','_time'])


def _convert_data(avg_1mo, avg_1d, last):
    logger.info("Converting data...")

    avg_1d_dict = {item['currency']: item['_value'] for item in avg_1d}
    avg_1mo_dict = {item['currency']: item['_value'] for item in avg_1mo}

    result = {}
    for item in last:
        currency = item['currency']
        result[currency] = {
            'last': item['_value'],
            'last_updated_at': item['_time'],
            'avg_1d': avg_1d_dict.get(currency),
            'avg_1mo': avg_1mo_dict.get(currency)
        }

    logger.info("Done.")
    return result


def get_data():
    logger.info("Start fetching data...")

    avg_1mo = loads(_query_storage(_query_avg_1mo))
    avg_1d = loads(_query_storage(_query_avg_1d))
    last = loads(_query_storage(_query_last))
    logger.info("Done.")

    return _convert_data(avg_1mo, avg_1d, last)
