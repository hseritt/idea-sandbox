#!/usr/bin/env python
"""
A logging demo that shows most of all you'll ever need to know
concerning Python and logging.
"""
import logging
import sys


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_format = logging.Formatter(
    '%(asctime)s  [%(levelname)s]  [%(module)s.%(name)s.%(funcName)s]:%(lineno)s' \
    '  %(message)s'
)

file_handler = logging.FileHandler(filename='log_demo.log', mode='w')
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)

class LogDemo(object):

    def run(self):
        logger.debug('Debug message.')
        logger.info('Info message.')
        logger.warning('Warning message.')
        logger.error('Error message.')
        logger.critical('Critical message.')

        
if __name__ == '__main__':

    demo = LogDemo()
    demo.run()
