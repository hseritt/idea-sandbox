#!/usr/bin/env python

import logging

logging.basicConfig(
	filename='demo2.log',
	filemode='w',
	level=logging.DEBUG,
	format='%(asctime)s %(levelname)s:%(module)s.%(name)s.%(funcName)s: %(message)s'
)

class LogDemo(object):

	logger = logging.getLogger('LogDemo')
	
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
