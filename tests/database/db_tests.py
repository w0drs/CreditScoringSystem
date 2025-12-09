from src.backend.database import Database

db = Database("../../data/database/applications.db")
client = db.get_client_by_id(123)
print(client)