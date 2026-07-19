from surrealdb import Surreal

from mentor.config import (
    SURREAL_URL,
    SURREAL_USERNAME,
    SURREAL_PASSWORD,
    SURREAL_NAMESPACE,
    SURREAL_DATABASE,
)


def get_db():
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

if __name__ == "__main__":
    db = get_db()
    db.query("""
        DEFINE TABLE memory SCHEMALESS;
        """)
    result = db.query("INFO FOR DB;")
    print("DB Connected successfully:", result)