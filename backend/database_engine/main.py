import json
from os import getenv
from sqlite3 import IntegrityError, DatabaseError
from urllib import response

import db_utilities as db_conn
import tables as tables
from flask import Flask, abort, jsonify, request
#from sql_query import SQL_QUERY
from sqlalchemy import func, select
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

app.config["DEVELOPMENT"] = getenv("DEVELOPMENT", default="local")
app.config["MYSQL_USER"] = getenv("MYSQL_USER", default="admin")
app.config["MYSQL_PASSWORD"] = getenv("MYSQL_PASSWORD", default="admin")
app.config["MYSQL_DATABASE"] = getenv("MYSQL_DATABASE", default="comp_db")
app.config["SQLALCHEMY_DATABASE_URI"] = db_conn.get_connection(
    app.config["MYSQL_USER"],
    app.config["MYSQL_PASSWORD"],
    app.config["MYSQL_DATABASE"],
    3306,
    version=app.config["DEVELOPMENT"])

db = tables.db

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """
    Index route handler
    """
    return "db!"

@app.errorhandler(HTTPException)
def handle_exception(e):
    """
    Error handler
    """
    return jsonify(str(e)), e.code

@app.route('/get_competitions_events', methods=["GET"])
def get_competitions() -> response:
    '''
    get all competitions
    '''
    return db.session.execute(select(tables.competitions)).all(), 200

# @app.route('/get_events', methods=["GET"])
# def get_events() -> response:
#     payload = request.json # get competition id
#     return db.session.execute(select(tables.events).
#                               where(tables.events.comp_id == payload['comp_id'])).all(), 200

@app.route('/create_tables', methods=['GET'])
def create_all_tbs() -> response:
    '''
    create_tables route. drops all existing tables and then creates all tables
    '''
    try:
        db.drop_all()
        db.create_all()
        with db.session.begin():
            # This creates mock data in the database:
            # for query in SQL_QUERY.split("\n"):
            #     db.session.execute(text(query))
            db.session.commit()
    except DatabaseError:
        abort(500, "Table(s) exist already.")
    return jsonify("Tables created"), 200

@app.route('/add_competition', methods=["POST"])
def add_competition() -> response:
    '''
    add competition to table
    '''
    payload = request.json # get competition payload
    competition = tables.competitions(**payload)
    with db.session.begin():
        try:
            db.session.add(competition)  # insert competition
        except IntegrityError:
            db.session.rollback()
            abort(
                500, "Could not add project to database")
        else:
            db.session.commit()
    return jsonify("Competition added"), 200

@app.route('/add_event', methods=["POST"])
def add_event() -> response:
    '''
    add event to table
    '''
    payload = request.json # get event payload
    event = tables.events(**payload)
    with db.session.begin():
        try:
            db.session.add(event)  # insert event
        except IntegrityError:
            db.session.rollback()
            abort(
                500, "Could not add project to database")
        else:
            db.session.commit()
    return jsonify("Event added"), 200

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8501, debug=True)
