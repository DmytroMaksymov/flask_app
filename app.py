#!python3
from flask import Flask, render_template
from flask import request
import datetime
from ua_parser import user_agent_parser

app = Flask(__name__)


@app.route("/whoami")
def whoami():
    user_ip = request.remote_addr
    browser = user_agent_parser.Parse(request.user_agent.string)['user_agent']['family']
    servertime = datetime.datetime.now()
    servertime = servertime.strftime("%H:%M:%S")
    return f"Your IP:  {user_ip}" \
           f"<br>Your browser: {browser}" \
           f"<br> Servertime : {servertime}</br>" \



@app.route('/source_code')
def source_code():
    with open("dz4.py", "r") as fo:
        return render_template('content.html', text=fo.read())


@app.route('/')
def hello():
    return 'Hello!' \
           '<br> Type "/whoami" to check your ip and servertime' \
           '<br>Type "/source_code" to check source_code'


if __name__ == '__main__':
    app.run(debug=True)
