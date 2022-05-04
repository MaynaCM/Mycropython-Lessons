from machine import Pin
from utime import sleep

btn = Pin(0, Pin.IN, Pin.PULL_DOWN)

while True: 
  btn_read = btn.value()
  print(btn_read)
  sleep(0.5)
