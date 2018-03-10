from flask import Flask, request, render_template
import redis
import os
import random

app = Flask(__name__)

redis_server = os.environ['REDIS'] if os.environ.has_key('REDIS') else 'localhost'
redis_cnn = redis.Redis(redis_server)

@app.route('/', methods=['GET'])
def index():
  try:
    visits = redis_cnn.incr('visits')
  except redis.ConnectionError:
    visits = 'N/A'
  return render_template("index.html", visits=visits)

@app.route('/book', methods=['GET'])
def book():
  name = request.args.get('name')
  path = 'books/' + name.lower()
  with open(path) as f:
    return "<br>".join(f.readlines())

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
