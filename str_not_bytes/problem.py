#!/usr/bin/env python

import subprocess
import sys

p = subprocess.Popen(
    ["ls", "-al"],
    stdout = subprocess.PIPE,
    stderr= subprocess.PIPE
) 


while True:
    nextline = p.stdout.readline()
    if not nextline and p.poll() is not None:
        break
    sys.stdout.write(nextline)
    sys.stdout.flush()


output = p.communicate()[0]
print(output)
exit_code = p.returncode
