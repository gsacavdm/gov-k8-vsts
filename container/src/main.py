from flask import Flask, request, render_template
import os
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/book', methods=['GET'])
def book():
  name = request.args.get('name')
  path = 'books/' + name.lower()
  with open(path) as f:
    return f.readlines().__str__()

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="5000")
