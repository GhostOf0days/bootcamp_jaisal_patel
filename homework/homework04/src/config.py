# Project config helpers

import os
from pathlib import Path

from dotenv import load_dotenv


def load_env():
    # Load key/value pairs from `.env`.
    load_dotenv()


def get_key(name, default=None):
    # Return an environment variable. Called after `load_env()`.
    return os.getenv(name, default)


PROJECT_ROOT = Path.cwd()
# Raw and processed data.
DATA_DIR = PROJECT_ROOT / "data"
