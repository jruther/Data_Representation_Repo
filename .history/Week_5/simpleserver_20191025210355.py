#follow along from Andrew's lab.  JR 25.10.19

#!flask/bin/python

from flask import Flask
app = Flask(_name_, static_url_path='', static_folder= '../')


@app.route('/')
def index():
    return "Hello, World!"
    
if _name_=='_main_' :
    app.run(debug = True)

    


