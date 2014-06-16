from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from util import *
#TODO sqlite3 db connection to store sudo pw, first time run, log locations etc
import sqlite3

app = Flask(__name__)

#Start SocketIO event handlers
@SocketIO.on('r_logs')
def get_logs():
    emit('logs_resp', {'data': logs.gh_log})

#End SocketIO event handlers

@app.route('/')
def main():

    return render_template("Main.html", user='Dhash')

"""@app.route('/disks')
def charts():"""


@app.route('/stats_and_logs')
def stats_and_logs():
    return render_template("stats_and_logs.html", logfile=logs.gh_log('/var/log/greyhole.log'))


if __name__ == '__main__':
    app.run()
