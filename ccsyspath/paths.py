import subprocess
from subprocess import PIPE
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
        p = subprocess.Popen(cmd, stdin=devnull, stdout=PIPE, stderr=PIPE)
        p.wait()
        lines = p.stderr.read()
        lines = lines.splitlines()
    return lines


def system_include_paths(compiler, cpp=True):
    extraflags = []
    if cpp:
        extraflags = b'-x c++'.split()
    lines = compiler_preprocessor_verbose(compiler, extraflags)

    idx = lines.index(b'#include <...> search starts here:')
    lines = lines[idx+1:-2]
    paths = []
    for line in lines:
        line = line.replace(b'(framework directory', b'')
        line = line.strip()
        paths.append(line)
    return paths 
