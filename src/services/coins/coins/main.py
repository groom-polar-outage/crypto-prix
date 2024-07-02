from loguru import logger
from coins.provider.coingecko import fetch_data
from coins.db.tsdb import store_data


def main():
    logger.info("START fetching data...")
    resp = fetch_data()
    logger.info("Done")

    logger.info("START storing data...")
    store_data(resp)
    logger.info("DONE")


if __name__ == "__main__":
    main()
