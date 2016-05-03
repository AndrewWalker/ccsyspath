import subprocess
from subprocess import PIPE
import os

def system_include_paths(compiler, cpp=True):
    lines = []
    with open(os.devnull, 'r') as devnull:
        cmd = [compiler, '-E'] 
        if cpp:
            cmd += ['-x', 'c++']
        cmd += ['-', '-v']
        p = subprocess.Popen(cmd, stdin=devnull, stdout=PIPE, stderr=PIPE)
        p.wait()
        lines = p.stderr.read()
        lines = lines.splitlines()

    idx = lines.index(b'#include <...> search starts here:')
    lines = lines[idx+1:-2]
    lines = [ line[1:] for line in lines ]
    paths = [ line.split(b' ')[0] for line in lines]
    return paths 
