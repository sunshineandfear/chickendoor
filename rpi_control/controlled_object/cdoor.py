import RPi.GPIO as GPIO
from .base import RaspObject

class Door(RaspObject):

	def __init__(self, channel, name=''):
		self.status = 'on'
		self.name = name
		super().__init__(channel)

	def switch(self, value):
		result = f'{self.name} is now '
		if value == 'open':
			a = 0
			while a < 200:
				GPIO.output(self.channel, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
				sleep(.01)
				GPIO.output(self.channel, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH. GPIO.LOW))
				sleep(.01)
				GPIO.output(self.channel, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
				sleep(.01)
				GPIO.output(self.channel, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
				sleep(.01)
				a += 1
			result = result + 'open'
		if value == 'close':
			a = 0
			while a < 200:
				GPIO.output(self.channel, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
				sleep(.01)
				GPIO.output(self.channel, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
				sleep(.01)
				GPIO.output(self.channel, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
				sleep(.01)
				GPIO.output(self.channel, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
				sleep(.01)
				a += 1
			result = result + 'closed'
		return result
