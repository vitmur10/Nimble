import csv
import psycopg2
from Const import *

connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)


def import_contacts_from_csv(csv_file, connection):
    with open(csv_file, "r") as file:
        # Зчитування CSV-файлу
        csv_reader = csv.reader(file)
        next(csv_reader)  # Пропустити заголовки

        # Інсерти даних в базу даних
        with connection.cursor() as cursor:
            for row in csv_reader:
                first_name, last_name, email = row
                cursor.execute("INSERT INTO contacts (first_name, last_name, email) VALUES (%s, %s, %s) "
                               "ON CONFLICT (email) DO UPDATE SET first_name = %s, last_name = %s",
                               (first_name, last_name, email, first_name, last_name))
        connection.commit()


# Підключення до бази даних


csv_file_path = "Nimble Contacts - Sheet1.csv"  # Шлях до вашого CSV-файлу
import_contacts_from_csv(csv_file_path, connection)
