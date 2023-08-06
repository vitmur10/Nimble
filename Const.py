url = "https://api.nimble.com/api/v1/contacts"
headers = {
    "Authorization": "Bearer NxkA2RlXS3NiR8SKwRdDmroA992jgu"
}
# Const.py

DB_NAME = "Nimble_db"
DB_USER = "postgres"
DB_PASSWORD = "uaprint"
DB_HOST = "localhost"
DB_PORT = "5432"

create_table_query = """
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE
);

"""
