print("Loading")
import time
#time.sleep(13)
#import state
#import view
import pwnagotchi.ui.driver
import random
import requests
#import time
#print(view.state)
name1 = "null"
face = "null1"
#print(face)
mylcd=pwnagotchi.ui.driver.lcd()
#mylcd.lcd_display_string("LOADING LCD",1,0)
def refresh():
   pass
#     mylcd.lcd_display_string("                ",1,0)
#     mylcd.lcd_display_string("                ",2,0)
#time.sleep(1)
#refresh()
part = 1
hor = 0
#time.sleep(1)
#def write(string):
#      mylcd.lcd_display_string(string,part,hor)
#      mylcd.lcd_display_string(face,2,5)
#write("( Q_Q)")

def write1(string):
    try:
        time.sleep(random.randint(10,15))
        refresh()
        url =  "http://127.0.0.1:8666/api/v1/mesh/data"
        headers = {}
        payload = {}
        response = requests.request("GET", url, headers=headers, data = payload)
        data = response.json()
        print(data)
        part = 2

        name1 = data["name"]
        hor = 5
        face = data["face"]
        print(data)
        # write(str(data['face']))
        mylcd.lcd_display_string(face+"                        ",2,16-len(face))
        mylcd.lcd_display_string(name1+"                        ",1,0)
    except Exception:
          print("LCD Face print failed")
          pass

    time.sleep(random.randint(10,15))
    hor = 15
#    write(str(random.randint(1,9)))
    part = 1
    inp = string
    length = len(inp)
#    refresh()
#    time.sleep(5)
    main = -1
    if length>15:
#        print("WO")
        for i in range(length+2):
            time.sleep(0.1)
            #print(inp[main:length])
            main = main+ 1
            mylcd.lcd_display_string(inp[main:length]+" "+" ",1,0)
#            print("GOING")
           # time.sleep(0.5)
    else:
          mylcd.lcd_display_string(inp[main:length]+" "+" ",1,0)

part = 1
#refresh()
print(face)
#write(name1)
#write(face)
#facel = len(face)
mylcd.lcd_display_string(name1,1,0)
mylcd.lcd_display_string(face,2,16-len(face))
print("DONE")
#exit()
"""

#refresh()
url =  "http://127.0.0.1:8666/api/v1/mesh/data"
headers = {}
payload = {}
response = requests.request("GET", url, headers=headers, data = payload)
data = response.json()
print(data)
part = 2
try:
    name1 = data["name"]
    hor = 5
    face = data["face"]
    print(data)
    # write(str(data['face']))
    mylcd.lcd_display_string(face+"                        ",2,16-len(face))
    mylcd.lcd_display_string(name1+"                        ",1,0)
except Exception:
    print("LCD Face print failed")
    pass



#time.sleep(3)
"""

