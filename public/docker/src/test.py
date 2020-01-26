#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
    return "Looks like it works!"

if __name__=='__main__':
    app.run()
