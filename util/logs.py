__author__ = 'dhash'
def gh_log(logfile):
    import commands
    last_100 = commands.getoutput('tail -n 100 ' + logfile)
    return last_100