import flask
from flask import request

app = flask.Flask(__name__)


def is_pyramid(word):
    if len(word) == 0:
        return False

    if not word.isalpha():
        return False

    count = [0] * (ord('z') - ord('a') + 1)

    for i in range(0, len(word)):
        count[ord(word[i]) - ord('a')] += 1
    count.sort()

    for i in range(0, len(count)):
        if count[i] == 0:
            continue
        if i > 0 and count[i] != count[i - 1] + 1:
            return False

    return True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Pyramid Word</h1><p>root</p>"


@app.route('/api/v1/ispyramidword', methods=['GET'])
def api_check_string():
    if 'string' in request.args:
        string = request.args['string'].lower()
    else:
        return "Error: No input string was provided."

    return str(is_pyramid(string))


app.run()
