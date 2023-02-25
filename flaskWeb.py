from flask import Flask
from flask import request
from threading import Thread
from waitress import serve

app = Flask('')

@app.route('/')
def home():
  return "I'm alive"

def run():
    serve(app, host="0.0.0.0", port=80)

def keep_alive():
  t = Thread(target=run)
  t.start()