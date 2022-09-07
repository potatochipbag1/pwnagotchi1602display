"""
#import state import view
import pwnagotchi.ui.driver
import random
import requests
import time
#print(view.state)
face = "null"
print(face)
mylcd=pwnagotchi.ui.driver.lcd()
exit()

#mylcd.lcd_display_string("LOADING LCD",1,0)
def refresh():
      mylcd.lcd_display_string("                ",1,0)
      mylcd.lcd_display_string("                ",2,0)
time.sleep(1)
refresh()
part = 1
hor = 0
#time.sleep(1)
def write(string):
    inp = string
    length = len(inp)
    main = -1
    if length>15:
#        print("WO")
        for i in range(length+1):
            time.sleep(0.2)
            #print(inp[main:length])
            main = main+ 1
            mylcd.lcd_display_string(inp[main:length]+"                        ",1,0)
           # time.sleep(0.5)
    else:
        mylcd.lcd_display_string(string,part,hor)
part = 1
def write1(string):
    inp = string
    length = len(inp)
    main = -1
    if length>15:
#        print("WO")
        for i in range(length+1):
            time.sleep(0.2)
            #print(inp[main:length])
            main = main+ 1
            mylcd.lcd_display_string(inp[main:length]+"                        ",1,0)
           # time.sleep(0.5)
    else:
          mylcd.lcd_display_string(inp[main:length]+"                        ",1,0)
part = 1
while(True):
      hor = 0
#      refresh()
      time.sleep(1)
      url =  "http://127.0.0.1:8666/api/v1/mesh/data"
      headers = {}
      payload = {}
      response = requests.request("GET", url, headers=headers, data = payload)
      data = response.json()
      part = 2
      hor = 5
      face = str(data["face"])
      write(face+"         ")
      hor = 15
      write(str(random.randint(1,9)))
      part = 1
      time.sleep(random.uniform(5.111,7.999))
#      write("xuehuapiaopiaobeifo")
      time.sleep(random.uniform(5.111,7.999))

"""

"""


"""
