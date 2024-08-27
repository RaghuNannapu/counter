import os
from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://redis:6379/0'

redis = FlaskRedis(app)

@app.route('/')
def counter():
    # Increment the Redis counter and get the value
    counter_value = redis.incr('web2_counter')
    
    # Get the message from the environment variable, default to an empty string if not set
    message = os.getenv('WEB2_COUNTER_MSG', '')
    
    # Return the formatted string
    return '{0} {1}'.format(counter_value, message)
