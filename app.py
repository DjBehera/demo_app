# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:53:18 2023

@author: dibyajyoti.b.behera
"""

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = False)

