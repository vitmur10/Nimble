import psycopg2

URL = "https://api.nimble.com/api/v1/contacts"
HEADERS = {
    "Authorization": "Bearer NxkA2RlXS3NiR8SKwRdDmroA992jgu"
}
create_table_query = """
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE
);

"""


def get_db_connection():
    return psycopg2.connect(
        dbname="Nimble_db",
        user="postgres",
        password="uaprint",
        host="localhost",
        port="5432"
    )


def add_contacts_to_db(cursor, first_name, last_name, email):
    cursor.execute("INSERT INTO contacts (first_name, last_name, email) VALUES (%s, %s, %s) "
                   "ON CONFLICT (email) DO UPDATE SET first_name = %s, last_name = %s",
                   (first_name, last_name, email, first_name, last_name))
