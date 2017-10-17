#!/usr/bin/env python

import logging
import sys


class LogDemo(object):

	logger = logging.getLogger('LogDemo')
	logger.setLevel(logging.DEBUG)

	log_format = logging.Formatter(
		'%(asctime)s  [%(levelname)s]  [%(module)s.%(name)s.%(funcName)s]  %(message)s  line #%(lineno)s')

	console_handler = logging.StreamHandler(sys.stdout)
	console_handler.setFormatter(log_format)
	logger.addHandler(console_handler)

	file_handler = logging.FileHandler(filename='demo3.log', mode='w')
	file_handler.setFormatter(log_format)
	logger.addHandler(file_handler)
	
	def my_func(self):
		try:
			division = 5 / 0
		except ZeroDivisionError as err:
			self.logger.exception(err)

	def run(self):
		self.logger.debug('This is a debug message. Just some developer info.')
		self.logger.info('This is an info message. Just some general info.')
		self.logger.warning('This is a warning message. Just to make you aware of a potential problem.')
		self.logger.error("This is an error message. You app won't work correctly if you don't fix this.")
		self.logger.critical("This is a critical message. Your app won't start if you don't fix this.")

		self.my_func()

		
if __name__ == '__main__':

	demo = LogDemo()
	demo.run()
