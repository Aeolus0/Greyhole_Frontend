#__author__ = 'dhash'
def restart(sudo_pw, process):
    import subprocess
    proc = subprocess.Popen(['sudo', 'service', process, 'restart'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    proc.stdin.write(sudo_pw + '\n')
    proc.stdin.close()
    out = proc.stdout()
    print out