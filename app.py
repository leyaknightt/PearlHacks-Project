from flask import Flask,json,request,send_file
import os
import urllib.request

app = Flask(__name__) # name refers to the module name


@app.route('/my-api',method = ['GET'])
def getInfo():
    url = "https://connect.myclimate.org"
    response = urllib.request.urlopen(url)
    return 


@app.route('/') # Python decorator, new syntax
def index():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=8000)

def about():
    return '<h1>about</h1>' 


