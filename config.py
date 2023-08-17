from rpi_control.controlled_object.cdoor import Door
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup((29,31,33,35,32,36,38,40), GPIO.OUT)

TWILIO_SMS_CONTROLLED_OBJECTS = {'Chickendoor': Door((29,31,33,35,32,36,38,40), 'Chickendoor')}
