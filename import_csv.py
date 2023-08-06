import csv
from Const import *

connection = get_db_connection()


def import_contacts_from_csv(csv_file, connection):
    with open(csv_file, "r") as file:
        # Зчитування CSV-файлу
        csv_reader = csv.reader(file)
        next(csv_reader)  # Пропустити заголовки

        # Інсерти даних в базу даних
        with connection.cursor() as cursor:
            for row in csv_reader:
                first_name, last_name, email = row
                add_contacts_to_db(cursor, first_name, last_name, email)

        connection.commit()


csv_file_path = "Nimble Contacts - Sheet1.csv"  # Шлях до вашого CSV-файлу
import_contacts_from_csv(csv_file_path, connection)
