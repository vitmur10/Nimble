from flask import Flask, request, jsonify
from psycopg2.extras import RealDictCursor
from Const import *

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def fulltext_search():
    search_text = request.args.get('text', '')

    # Пошук контактів з використанням full-text пошуку
    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=RealDictCursor)

    # Запит на пошук контактів
    query = """
        SELECT * FROM contacts
        WHERE to_tsvector('simple', first_name || ' ' || last_name || ' ' || email) @@ to_tsquery('simple', %s)
    """

    cursor.execute(query, (search_text,))
    contacts = cursor.fetchall()

    connection.close()

    return jsonify(contacts)


if __name__ == '__main__':
    app.run(debug=True)
