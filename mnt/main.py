#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""

"""

from flask import Flask, render_template, jsonify, request, session, redirect
from config import Config
from login import register_user, login_user, message_format
from Trivia import Trivia
app = Flask(__name__)

### possible games
games = {
    'Trivia':Trivia
}
current_games = {}


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Logged in as {username}'
    return "Not logged in"

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route('/login', methods=['POST'])
def login():
    if 'PersonID' in session:
        return redirect('gameID')

    data = request.json
    username = data['username']
    password = data['password']
    if PersonID := login_user(username, password):
        session['username'] = username
        session['PlayerID'] = PersonID
        return message_format('Successfully logged in.')
    else: return message_format('Incorrect password')
    

@app.route('/foo', methods=['POST', 'GET']) 
def foo():
    data = request.json
    return jsonify(data)

@app.route('/register', methods=['POST']) 
def register():
    data = request.json
    username = data['username']
    password = data['password']
    if PlayerID := register_user(username, password):
        session['username'] = username
        session['PlayerID'] = PersonID
        return message_format(f'Successfully created user {username}')
    else: return message_format(f'Failed to create user {username}')

@app.route('/info', methods=['GET', 'POST'])
def info():
    data = request.json
    username = session['username']
    if request.method == "GET":
        return get_info(username)
    elif request.method == "POST":
        return post_info(username, data)


@app.route('/new_game', methods=['POST'])
def new_game():
    data = request.json
    username = session['username']
    game_type = data['game']

if __name__== '__main__':
    app.config.from_object(Config)
    app.run(host='0.0.0.0', debug=True, port=5000)
