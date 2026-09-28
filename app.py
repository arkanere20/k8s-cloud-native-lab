from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", 6379))
redis_password = os.environ.get("REDIS_PASSWORD", None)

cache = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

@app.route("/")
def home():
    count = cache.incr("visits")
    return f"Hello from Docker! This page has been visited {count} times.\n"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
