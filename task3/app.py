# app.py
from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, db=0)

# Initialize Redis with "hello world"
try:
    if not redis_client.exists('message'):
        redis_client.set('message', 'hello world')
except Exception as e:
    print(f"Redis connection error: {e}")

@app.route('/')
def hello():
    try:
        message = redis_client.get('message')
        if message:
            return message.decode('utf-8')
        else:
            return "Redis key not found"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
