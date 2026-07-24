from mentor.database.surreal import get_db

    db = get_db()
    db.query("""
        DEFINE TABLE memory SCHEMALESS;
        """)
    result = db.query("INFO FOR DB;")
    print("DB Connected successfully:", result)