#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 master <master@master>
#
# Distributed under terms of the MIT license.

"""

"""

from sql import engine
import pandas as pd

df = pd.read_csv('trivial_all.csv')
df.to_sql(con=engine, name='new_trivia_all')
