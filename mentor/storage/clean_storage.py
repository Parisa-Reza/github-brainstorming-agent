from mentor.database.surreal import get_db


def main():

    db = get_db()

    db.query(
        "DELETE repository;"
    )

    db.query(
        "DELETE chunk;"
    )

    print("Database cleaned")


if __name__ == "__main__":
    main()