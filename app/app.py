import os

import psycopg
from flask import Flask

app = Flask(__name__


@app.route("/")
def home():
    database_url = os.environ["DATABASE_URL"]

    with psycopg.connect(database_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT message FROM app_status ORDER BY id DESC LIMIT 1"
            )
            result = cursor.fetchone()

    if result:
        return result[0]

    return "No status message found in PostgreSQL."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
