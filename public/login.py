#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""

"""

from sql import engine, sql_value
from passlib.hash import sha256_crypt
import pandas as pd
from flask import session

def register_user(username, password):
    p = sha256_crypt.encrypt(password)
    df = pd.DataFrame({"username":[username], "passwordHash":[p]})
    q = f"SELECT COUNT(username) FROM Players WHERE username = '{username}'"
    count = sql_value(q)
    if count == 0:
        df.to_sql('Players' ,con=engine, if_exists='append', index=False)
        PlayerID = get_PlayerID(username)
        return int(PlayerID)
    else: return False

def login_user(username, password):
    PlayerID = get_PlayerID(username)
    if PlayerID is None: return message_format(f'{username} does not exist.')
    q = f"SELECT passwordHash from Players WHERE PlayerID = {PlayerID}"
    h = sql_value(q)
    if sha256_crypt.verify(str(password), str(h)):
        ### successully logged in
        return int(PlayerID)
    else: return False

def get_PlayerID(username):
    q = f"SELECT playerID FROM Players WHERE username = '{username}' ORDER BY playerID ASC LIMIT 1"
    PlayerID = sql_value(q)
    return PlayerID

def message_format(msg):
    out = "{'message':'" + str(msg) + "'}"
    return out
