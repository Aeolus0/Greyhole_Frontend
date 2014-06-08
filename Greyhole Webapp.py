from flask import Flask, render_template
from util import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("Main.html", user='Dhash')

"""@app.route('/disks')
def charts():"""


@app.route('/stats_and_logs')
def stats_and_logs():
    return render_template("stats_and_logs.html", logfile=logs.gh_log('/var/log/greyhole.log'))


if __name__ == '__main__':
    app.run()
