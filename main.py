import os

from flask import Flask, request
from dotenv import load_dotenv

from src.api_wraper import ApiWrapper


app = Flask(__name__)


@app.route('/get-users')
def search():
    wrapper = ApiWrapper(client_id, client_secret)
    query = request.args.get('query')


    if not query:
        return {"error": "Query not provided"}

    users = wrapper.search_users(query)

    return {"result": {user.id: user.username for user in users}}


if __name__ == '__main__':
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    app.run()
