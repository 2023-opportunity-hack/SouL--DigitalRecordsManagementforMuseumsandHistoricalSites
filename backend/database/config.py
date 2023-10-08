# ELASTIC SEARCH LOGIN CONFIGS
from .runnable_configs import ENVIRONMENT


# TODO (rohan): move to env vars
KEY_PATH = "../fernetKey.key"
USER_NAME = "test"
PASSWORD = b'gAAAAABlIg0vQSh48oNMLQf8L0cSKXBUUfmvKJY75WKCEMJn7jP6WR9YtR0xhJk7SUWfOPGRz8vCY0OSbYgt9mmXR6lYGJ9e1g=='

# ELASTIC SEARCH CLASS CONFIGS
HOST = "localhost"
PORT = 9200
URL = f"http://{HOST}:{PORT}"

# CONFIGS DEPENDEDNT ON ENVRONMENT
if ENVIRONMENT.lower() == "dev":
    INDEX_NAME = "search_index_dev"
else:
    INDEX_NAME = "search_index_prod"

