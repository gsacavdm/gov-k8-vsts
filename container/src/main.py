from flask import Flask, request, render_template
import redis
import os
import random

app = Flask(__name__)

VISITS_NAME = 'visits'

redis_server = os.environ['REDIS'] if os.environ.has_key('REDIS') else 'localhost'
redis_cnn = redis.Redis(redis_server)

def test_redis():
  try:
    redis_cnn.get(VISITS_NAME)
    return True
  except redis.ConnectionError:
    pass
  return False

@app.route('/', methods=['GET'])
def index():
  visits = 'N/A'
  
  if redis_on:
    try:
      visits = redis_cnn.incr(VISITS_NAME)
    except redis.ConnectionError:
      pass

  return render_template("index.html", visits=visits)

@app.route('/book', methods=['GET'])
def book():
  name = request.args.get('name')
  path = 'books/' + name.lower()
  with open(path) as f:
    return "<br>".join(f.readlines())

@app.route('/redis_check', methods=['GET'])
def redis_check():
  redis_on = test_redis()
  if (redis_on):
    return "On"
  else:
    return "Off"

if __name__ == "__main__":
  redis_on = test_redis()
  app.run(host="0.0.0.0", port=5000)