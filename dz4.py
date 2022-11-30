#!python3
from flask import Flask, render_template, request
import datetime
from ua_parser import user_agent_parser
import random
import string

app = Flask(__name__)


@app.route("/whoami")
def whoami():
    """return user's ip, browser and server time"""
    user_ip = request.remote_addr
    browser = user_agent_parser.Parse(request.user_agent.string)['user_agent']['family']
    servertime = datetime.datetime.now()
    servertime = servertime.strftime("%H:%M:%S")
    return f"Your IP:  {user_ip}" \
           f"<br>Your browser: {browser}" \
           f"<br> Servertime : {servertime}</br>" \



@app.route('/source_code')
def source_code():
    """read and show source-code file"""
    with open("dz4.py", "r") as fo:
        return render_template('content.html', text=fo.read())


@app.route('/random', methods=['GET', 'POST'])
def a():
    """get user's parameters where lenght = count symbols,
    specials and digits are boolean type, if bool=True add them to random string"""
    length = request.args.get('length', type=int)
    specials = request.args.get('specials', type=int)
    digits = request.args.get('digits', type=int)

    # blocks with checking user's parameters
    if 1 < length < 100 and specials == 1 and digits == 1:
        message = ''.join(random.choice(string.ascii_lowercase + string.digits
                                        + string.punctuation) for _ in range(length))
        return message
    elif 1 < length < 100 and specials == 1:
        message = ''.join(random.choice(string.ascii_lowercase + string.punctuation) for _ in range(length))
        return message
    elif 1 < length < 100 and digits == 1:
        message = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
        return message
    elif 1 < length < 100:
        message = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return message
    else:
        return 'Error, try again'


@app.route('/')
def hello():
    return '<h1>Hello there!</h1>' \
           'Type "/whoami" to check your ip, browser and servertime<br>' \
           '<br>Type "/source_code" to check application source code<br>' \
           '<h4>Type "/random?length=42&specials=0&digits=0" to create random string</h4>' \
           'Where length is count of symbols' \
           '<br>if you want to add digits (0-9) -> type digits=1' \
           '<br>if you want to add specials symbols (!"#$%&()*\+,-./:;<=>?_@[]^`{|}~) -> type specials=1' \
           '<br>if you do not want to add these parameters -> type digits=0 and specials=0'


if __name__ == '__main__':
    app.run(debug=True)
