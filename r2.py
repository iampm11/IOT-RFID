#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import RPi.GPIO as IO
import time
import mechanize

def blink():
    IO.setmode(IO.BCM)
    IO.setup(21,IO.OUT)
    IO.output(21,1)
    time.sleep(0.5)
    IO.output(21,0)

def fenkde():
    br = mechanize.Browser()
    br.open("http://pi.pmanaktala.com/messages.php")
    br.form = list(br.forms())[0]
    br.form['tagid'] = str(id)
    br.form['name'] = name
    br.form['quantity'] = quantity
    br.form['batch'] = batch
    br.form['pid'] = pid
    req = br.submit()

id = 0
name =''
quantity=''
batch=''
pid=''
reader = SimpleMFRC522.SimpleMFRC522()

try:
        id, text = reader.read()
        blink()
        print(id)
        name,quantity,batch,pid=text.split(",")
        print("---------Data Read----------")
        print("Name of item :" + name)
        print("Quantity :" + quantity)
        print("Batch Number :" + batch)
        print("Product id :" + pid)
        fenkde()
        print("---------Data Updated----------")
finally:
    GPIO.cleanup()
