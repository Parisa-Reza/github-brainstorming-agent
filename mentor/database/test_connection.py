
from mentor.database.surreal import get_db


def main():
    print("Starting connection test...")

    db = get_db()

    print("Connected successfully")

    result = db.query("INFO FOR DB;")

    print("Query executed")
    print(result)


if __name__ == "__main__":
    main()