from requests import get
from requests.exceptions import HTTPError, Timeout, ConnectionError, RequestException
from json import loads

from loguru import logger

from coins.config import CONFIG


cg_headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": CONFIG.COINGECKO_API_KEY,
}
cg_url = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin"
    "&vs_currencies=usd%2Cczk"
    "&include_last_updated_at=true"
    "&precision=5"
)


def fetch_data() -> dict:
    try:
        r = get(cg_url, headers=cg_headers)
        r.raise_for_status()

        if r.status_code == 200:
            logger.info(f"Fetched data: {r.text}")
            return loads(r.text)
        else:
            raise NotImplementedError

    except Timeout as errt:
        logger.error(f"Timeout Error: {errt.response.text}")
    except ConnectionError as errc:
        logger.error(f"Error Connecting: {errc.response.text}")
    except HTTPError as errh:
        logger.error(f"Http Error: {errh.response.text}")
    except RequestException as err:
        logger.error(f"Request Error: {err.response.text}")
