#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""

"""

from flask import Flask, render_template, jsonify, request, session, redirect, send_from_directory
from config import Config
from login import register_user, login_user, message_format, dest_format, logged_in
from Trivia import Trivia
from get_key import get_key
from sql import engine
app = Flask(__name__)

### possible games
games = {
    'Trivia':Trivia
}
current_games = {}


@app.route('/')
def index():
    if logged_in(): return render_static('/hostOrJoin')

    return render_template('index.html')
    #  if 'username' in session:
        #  username = session['username']
        #  return f'Logged in as {username}'
    #  return "Not logged in"



@app.route('/<string:page_name>/')
def render_static(page_name):
    #  return send_from_directory(app.config['RESULT_STATIC_PATH'], f"{page_name}.html")
    return render_template(f'{page_name}.html')

@app.route('/login_user', methods=['POST'])
def login():
    if logged_in(): return render_static('/hostOrJoin')

    data = request.json
    username = request.form['username']
    password = request.form['password']
    if PersonID := login_user(username, password):
        session['username'] = username
        session['PlayerID'] = PersonID
        return dest_format("/hostOrJoin")
        #  return redirect('phoneGame')
        #  return message_format('Successfully logged in.')
    else: return message_format('Incorrect password')

@app.route('/register_user', methods=['POST']) 
def register():
    if logged_in(): return render_static('/hostOrJoin')
    #  data = request.json
    data = request.form
    username = data['username']
    password = data['password']
    if PlayerID := register_user(username, password):
        session['username'] = username
        session['PlayerID'] = PersonID
        return dest_format('hostOrJoin')
        #  return message_format(f'Successfully created user {username}')
    else: return message_format(f'Failed to create user {username}')

@app.route('/info', methods=['GET', 'POST'])
def info():
    #  if not logged_in(): return render_template('/index.html')
    data = request.json
    key = session['key']
    username = session['username']
    if key in current_games:
        if request.method == "GET":
            return current_games[key].get_info(username)
        elif request.method == "POST":
            return current_games[key].post_info(data, username)
    else:
        return message_format("Game not valid.")

@app.route('/new_game', methods=['POST'])
def new_game():
    if not logged_in(): render_static('/login')
    data = request.json
    username = session['username']
    game_type = request.form['game']
    key = get_key(current_games)
    if game_type in games:
        current_games[key] = games[game_type](engine, key)
        session['key'] = key
        return dest_format('/hostGame')
    else: return message_format('Invalid game type')

@app.route('/join_game', methods=['POST'])
def join_game():
    #  data = request.json
    data = request.form
    username = session['username']
    key = data["gameid"]

    if key in current_games:
        session['key'] = key
        session['gameid'] = key
        current_games[key].add_player(username)
        return dest_format('/phoneGame')
    else: return message_format('Invalid game type')



if __name__== '__main__':
    app.config.from_object(Config)
    app.run(host='0.0.0.0', debug=True, port=5000)
