from flask import Flask, request
import logging
from statsd import StatsClient

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
                    handlers=[logging.StreamHandler()])

app.logger.setLevel(logging.DEBUG)

# Configure StatsD
statsd_client = StatsClient(host='localhost', port=8125, prefix='your_app')

@app.before_request
def before_request():
    app.logger.debug('Request received: %s', request.path)
    statsd_client.incr('requests')

@app.teardown_request
def teardown_request(exception):
    if exception:
        app.logger.error('Exception occurred: %s', exception)
        statsd_client.incr('exceptions')

@app.route('/')
def home():
    app.logger.info('Home endpoint accessed')
    return 'Hello, Flask!'

@app.route('/error')
def error():
    app.logger.error('Error endpoint accessed')
    raise Exception('This is a test exception')

if __name__ == '__main__':
    app.run(debug=True)