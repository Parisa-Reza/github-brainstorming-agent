
import os
from surrealdb import Surreal

from mentor.config import (
    SURREAL_URL,
    SURREAL_USERNAME,
    SURREAL_PASSWORD,
    SURREAL_NAMESPACE,
    SURREAL_DATABASE,
)


def get_db():
    # Disable proxy only for localhost SurrealDB
    old_http = os.environ.pop("HTTP_PROXY", None)
    old_https = os.environ.pop("HTTPS_PROXY", None)
    old_http_l = os.environ.pop("http_proxy", None)
    old_https_l = os.environ.pop("https_proxy", None)
    old_no = os.environ.pop("NO_PROXY", None)
    old_no_l = os.environ.pop("no_proxy", None)

    try:
        db = Surreal(SURREAL_URL)

        db.signin(
            {
                "username": SURREAL_USERNAME,
                "password": SURREAL_PASSWORD,
            }
        )

        db.use(
            SURREAL_NAMESPACE,
            SURREAL_DATABASE,
        )

        return db

    finally:
        if old_http:
            os.environ["HTTP_PROXY"] = old_http
        if old_https:
            os.environ["HTTPS_PROXY"] = old_https
        if old_http_l:
            os.environ["http_proxy"] = old_http_l
        if old_https_l:
            os.environ["https_proxy"] = old_https_l
        if old_no:
            os.environ["NO_PROXY"] = old_no
        if old_no_l:
            os.environ["no_proxy"] = old_no_l