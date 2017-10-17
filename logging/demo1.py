#!/usr/bin/env python

import logging

logging.basicConfig(filename='demo1.log', filemode='w', level=logging.DEBUG)
logging.debug('This is a debug message.')
logging.info('This is an info message.')
logging.warning('This is a warning message.')
