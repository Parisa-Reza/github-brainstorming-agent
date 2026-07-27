from mentor.database.surreal import get_db

db = get_db()

db.query("DEFINE TABLE repository SCHEMALESS;")
db.query("DEFINE TABLE chunk SCHEMALESS;")
db.query("DEFINE TABLE memory SCHEMALESS;")
db.query("DEFINE TABLE conversation SCHEMALESS;")

print("Database initialized.")
result = db.query("INFO FOR DB;")
print("DB Connected successfully:", result)