from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.domain.write_precision import WritePrecision
from pendulum import from_timestamp

from coins.config import CONFIG


client = InfluxDBClient(
    url=CONFIG.TSDB_URL, token=CONFIG.TSDB_TOKEN, org=CONFIG.TSDB_ORG
)


def store_data(provider_data: dict) -> Any:
    coin, data = provider_data.popitem()

    points = []
    for currency in ["usd", "czk"]:
        points.append(
            Point(measurement_name=coin)
            .tag("currency", currency)
            .field("price", data[currency])
            .time(
                from_timestamp(
                    int(data["last_updated_at"]), tz=CONFIG.TIMEZONE
                ).to_rfc3339_string(),
                write_precision=WritePrecision.S,
            )
        )

    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket=CONFIG.TSDB_BUCKET, org=CONFIG.TSDB_ORG, record=points)
