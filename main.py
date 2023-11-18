import os

from flask import Flask, request
from dotenv import load_dotenv

from src.api_wraper import ApiWrapper

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

app = Flask(__name__)


@app.route('/get-users')
def search():
    wrapper = ApiWrapper(CLIENT_ID, CLIENT_SECRET)
    query = request.args.get('query')

    if not query:
        return {"error": "Query not provided"}

    users = wrapper.search_users(query)

    return {"result": [user.model_dump_json()] for user in users}

    # return {"result": {
    #     "avatar_url": user.avatar_url,
    #     "id": user.id,
    #     "username": user.username
    # } for user in users}
