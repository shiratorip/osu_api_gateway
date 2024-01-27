import os

from flask import Flask, request
from dotenv import load_dotenv

from src.api_wraper import ApiWrapper

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

app = Flask(__name__)


# test curl "http://127.0.0.1:5000/search?q=chocomint&mode=all&page=1"

@app.route('/scores')
def get_scores():
    wrapper = ApiWrapper(CLIENT_ID, CLIENT_SECRET)
    user = request.args.get("user")
    return wrapper.get_scores()

@app.route('/search')
def search():
    wrapper = ApiWrapper(CLIENT_ID, CLIENT_SECRET)
    query = request.args.get('q')
    mode = request.args.get('mode') or 'all'
    page_from_request = request.args.get('page') or '1'


    if not query:
        return {"error": "Query not provided"}

    if page_from_request.isdigit():
        page = int(page_from_request)
    else:
        return {"error": "Invalid page"}

    print(query, " ", mode, " ", page)

    # items = wrapper.search_wiki(query)
    if mode == 'user':
        items = wrapper.search_users(query=query, page=page)
        return [user.model_dump() for user in items]
        
    elif mode == 'wiki':
        items = wrapper.search_wiki(query=query, page=page)
        return [wiki.model_dump() for wiki in items]
        
    else:
        users, wiki = wrapper.search_all(query=query, page=page)
        return [[user.model_dump() for user in users],
            [wiki.model_dump() for wiki in wiki]]
