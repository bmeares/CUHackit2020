#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""

"""

import MySQLdb
import sqlalchemy
import pandas as pd
engine = sqlalchemy.create_engine('mysql+pymysql://cuhackit2020:gurgle@inscribe.productions/hackbox_db')

def sql_value(query):
    try:
        df = pd.read_sql_query(query, engine)
        out = df.iloc[0, 0]
    except:
        print('Error! Failed to execute query:')
        print(f'{query}')
        return None
    else:
        return out

def exec_sql(query):
    return pd.read_sql_query(query, engine)
