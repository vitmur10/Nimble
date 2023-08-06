import requests
from Const import *
import schedule
import time


def get_nimble_contacts():
    response = requests.get(URL, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch Nimble contacts.")
        return None


def update_database_with_contacts():
    nimble_contacts = get_nimble_contacts()

    if nimble_contacts:
        # Підключення до бази даних
        connection = get_db_connection()
        # Оновлення контактів у базі даних
        with connection.cursor() as cursor:
            for contact in nimble_contacts['resources']:
                first_name = contact['fields'].get('first name', [{}])[0].get('value', '')
                last_name = contact['fields'].get('last name', [{}])[0].get('value', '')
                email = contact['fields'].get('email', [{}])[0].get('value', '')
                add_contacts_to_db(cursor, first_name, last_name, email)

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
