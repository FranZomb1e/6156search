from flask import *
import database_services.RDBService as d_service
from flask_cors import CORS
import json

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from application_services.cat_resource import CatResource
from application_services.BreederResource.breeder_service import BreederResource


app = Flask(__name__)
CORS(app)


@app.route('/')
def main_page():
    return render_template('simple-test.html')




@app.route('/breeders/<bid>/<name>/<organization>/<phone>/<email>/<address>/<website>/<rating>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def breeders(bid, name, organization, phone, email, address, website, rating):
    if request.method == 'GET':
        res = BreederResource.get_by_template(None)
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
        return rsp
    if request.method == 'POST':
        res = BreederResource.post_breeder(bid, name, organization, phone, email, address, website, rating)
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
        return rsp

@app.route('/breeders/rating', methods=['GET', 'POST', 'PUT', 'DELETE'])
def breede_rating():
    if request.method == 'GET':
        breeder_id = request.args.get('bid', default='1')
        res = BreederResource.get_breeder_rating(breeder_id)
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
        return rsp

@app.route('/cats/<cid>/<race>/<color>/<dob>/<father>/<mother>/<breeder>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def cats(cid, race, color, dob, father, mother, breeder):
    if request.method == 'GET':
        res = BreederResource.get_by_template(None)
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
        return rsp
    if request.method == 'POST':
        res = CatResource.post_cat(cid, race, color, dob, father, mother, breeder)
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
        return rsp

@app.route('/cats/breeder/<cid>')
def breeder_of_cat(cid):
    res = CatResource.get_breeder_id(cid)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")


# @app.route('/imdb/artists/<prefix>')
# def get_artists_by_prefix(prefix):
#     res = IMDBArtistResource.get_by_name_prefix(prefix)
#     rsp = Response(json.dumps(res), status=200, content_type="application/json")
#     return rsp

# @app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
# def get_by_prefix(db_schema, table_name, column_name, prefix):
#     res = d_service.get_by_prefix(db_schema, table_name, column_name, prefix)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
