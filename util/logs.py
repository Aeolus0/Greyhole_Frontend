__author__ = 'dhash'
def gh_log(logfile):
    import commands
    #TODO sanitize logfile, as stands allows for arbitrary code injection
    last_100 = commands.getoutput('tail -n 100 ' + logfile)
    return last_100

def view_queue():
    import commands
    current_queue = commands.getoutput('greyhole --view-queue')
    return current_queue

def iostat():
    import commands
    return commands.getoutput('greyhole --iostat')
