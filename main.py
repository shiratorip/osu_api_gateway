import os

from flask import Flask, request
from dotenv import load_dotenv

from src.api_wraper import ApiWrapper

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

app = Flask(__name__)


# test curl "http://127.0.0.1:5000/search?q=chocomint&mode=wiki&page=1"
@app.route('/search')
def search():
    wrapper = ApiWrapper(CLIENT_ID, CLIENT_SECRET)
    query = request.args.get('q')
    mode = request.args.get('mode')
    page = request.args.get('page')
    print(query, " ", mode, " ", page)
    if not query:
        return {"error": "Query not provided"}
    if not page:
        page = 1
    if not mode:
        mode = 'all'

    # items = wrapper.search_wiki(query)
    if mode == 'user':
        items = wrapper.search(query=query, page=int(page), mode='user')
    elif mode == 'wiki':
        items = wrapper.search(query=query, page=int(page), mode='wiki_page')
    else:
        items = wrapper.search(query=query, page=int(page), mode='all')

    return [item.model_dump() for item in items]
