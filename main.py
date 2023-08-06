import requests
from Const import *
import schedule
import time


def get_nimble_contacts():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch Nimble contacts.")
        return None


def update_database_with_contacts():
    nimble_contacts = get_nimble_contacts()

    if nimble_contacts:
        # Підключення до бази даних
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        # Оновлення контактів у базі даних
        with connection.cursor() as cursor:
            for contact in nimble_contacts['resources']:
                first_name = contact['fields'].get('first name', [{}])[0].get('value', '')
                last_name = contact['fields'].get('last name', [{}])[0].get('value', '')
                email = contact['fields'].get('email', [{}])[0].get('value', '')
                cursor.execute("INSERT INTO contacts (first_name, last_name, email) VALUES (%s, %s, %s) "
                               "ON CONFLICT (email) DO UPDATE SET first_name = %s, last_name = %s",
                               (first_name, last_name, email, first_name, last_name))

        connection.commit()
        connection.close()

        print("Contacts updated successfully.")


update_database_with_contacts()
# Розкоментуйте наступний рядок, якщо хочете виконувати оновлення щоденно о 00:00
# schedule.every().day.at("00:00").do(update_database_with_contacts)

# Розкоментуйте наступний рядок, якщо хочете виконувати оновлення кожні 24 години
schedule.every(24).hours.do(update_database_with_contacts)

while True:
    schedule.run_pending()
    time.sleep(1)
