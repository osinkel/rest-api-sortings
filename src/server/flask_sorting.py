from flask import request, Flask
from src.controllers.sorting_controller import add_sort_to_db, get_all
from src.config import settings
from src.utils.json_parser import ORJSONDecoder, ORJSONEncoder


app = Flask(__name__)


@app.route('/')
def index():
    return "Flask app is working!"


@app.route('/sort/<name>', methods=['POST', 'GET'])
def sort_nums_cache(name):
    if request.method == 'POST':
        seq = request.json['seq']
        res = add_sort_to_db(name, seq)
        return {'result': res['result'], 'time': res['time']}
    return ''


@app.route('/sequences')
def get_all_seq():
    return get_all()


def create_flask_app():
    app.json_encoder = ORJSONEncoder
    app.json_decoder = ORJSONDecoder
    return app


if __name__ == '__main__':
    create_flask_app().run(debug=True, host=settings.HOST, port=settings.PORT)
