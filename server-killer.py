import os
import sys

def killer(pid):
    os.popen(f'kill -9 {pid}')

def search(port):
    stream = os.popen(f'netstat -nlp | grep :{port}')
    output = list(filter(None, stream.read().split(' ')))
    for e in output:
        if '/' in e:
            e = e.split('/')
            pid = e[0]
            killer(pid)

def check_arguments():
    if len(sys.argv) != 2:
        print("Usage: srvkill [port] \nE.g. 'srvkill 3000' to kill server on port 3000")
    else:
        search(sys.argv[1])

check_arguments()

