#__author__ = 'dhash'
def restart(sudo_pw, process):

    #TODO sanitize the process input, right now vulnerable arbitrary code finjection

    import subprocess
    proc = subprocess.Popen(['sudo', 'service', process, 'restart'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    proc.stdin.write(sudo_pw + '\n')
    proc.stdin.close()
    out = proc.stdout()
    return out
