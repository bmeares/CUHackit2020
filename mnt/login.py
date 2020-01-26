#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""

"""

from sql import engine, sql_value
from passlib.hash import sha256_crypt
import pandas as pd
def register_user(username, password):
    p = sha256_crypt.encrypt(password)
    df = pd.DataFrame({"username":[username], "passwordHash":[p]})
    q = f"SELECT COUNT(username) FROM Players WHERE username = '{username}'"
    count = sql_value(q)
    print('count:', count)
    if count == 0:
        print(f'Creating user {username}')
        df.to_sql('Players' ,con=engine, if_exists='append', index=False)
        return f"Created {username}"
    else: return f"{username} already exists."

