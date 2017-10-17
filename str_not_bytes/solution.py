#!/usr/bin/env python

import subprocess
import sys


if __name__ == '__main__':

	p = subprocess.Popen(
	    ["ls", "-al"],
	    stdout = subprocess.PIPE,
	    stderr= subprocess.PIPE
	) 


	while True:
	    line = p.stdout.readline()
	    if line == b'' and p.poll() is not None:
	        break
	    
	    sys.stdout.write(line.decode('utf-8'))

	    # or
		# sys.stdout.write(line.decode(sys.stdout.encoding))

	    sys.stdout.flush()


	output = p.communicate()[0]
	print(output)
