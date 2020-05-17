from flask import jsonify

from init import create_app
from services.indexer import Indexer

import time
import threading
import requests

app = create_app()

@app.route('/index')
def index():
    Indexer().start()
    return jsonify(True), 200


def start_indexer():
    def start_loop():
        not_started = True
        while not_started:
            try:
                r = requests.get('http://127.0.0.1:11000/index')
                if r.status_code == 200:
                    not_started = False
            except:
                print('Server not yet started')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()


if __name__ == '__main__':
    start_indexer()
    app.run(host='0.0.0.0', port=11000)