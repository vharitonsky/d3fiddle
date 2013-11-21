import time
import random
from gevent import monkey; monkey.patch_all()
from bottle import route, run, response, static_file

controllers = ['c1', 'c2', 'c3']


def event_generator():
    while True:
        time.sleep(3)
        controller = random.choice(controllers)
        yield (
            "event: action\n"
            "data: %s\n"
            "\n\n"
        ) % controller

@route('/')
def index():
    return open('index.html').read()

@route('/sse')
def sse():
    return open('sse.html').read()

@route('/letters')
def letters():
    return open('letters.html').read()

@route('/ripples')
def ripples():
    return open('ripples.html').read()

@route('/repo')
def repo():
    return open('repo.html').read()

@route('/static/<path:path>')
def callback(path):
    return static_file(path, 'static')


@route('/events')
def events():
    response.headers['Content-Type'] = 'text/event-stream'
    return event_generator()


run(host='127.0.0.1', port=8080, server='gevent')
