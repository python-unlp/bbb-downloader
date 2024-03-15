from os import environ
from src import gmtv


if __name__ == "__main__":
    hash = environ.get("CODE")
    gmtv.run(hash)
