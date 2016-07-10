import subprocess
from subprocess import Popen, PIPE
import os
import re

def compiler_preprocessor_verbose(compiler, extraflags):
    """Capture the compiler preprocessor stage in verbose mode
    """
    lines = []
    with open(os.devnull, 'r') as devnull:
        cmd = [compiler, '-E'] 
        cmd += extraflags
        cmd += ['-', '-v']
        p = Popen(cmd, stdin=devnull, stdout=PIPE, stderr=PIPE)
        p.wait()
        p.stdout.close()
        lines = p.stderr.read()
        lines = lines.decode('utf-8')
        lines = lines.splitlines()
    return lines


def system_include_paths(compiler, cpp=True):
    extraflags = []
    if cpp:
        extraflags = '-x c++'.split()
    lines = compiler_preprocessor_verbose(compiler, extraflags)
    lines = [ line.strip() for line in lines ]

    start = lines.index('#include <...> search starts here:')
    end   = lines.index('End of search list.')

    lines = lines[start+1:end]
    paths = []
    for line in lines:
        line = line.replace('(framework directory)', '')
        line = line.strip()
        paths.append(line.decode('utf-8'))
    return paths 
