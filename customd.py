import pwnagotchi.ui.driver
import time
import os
#os.system("python3 /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/driver.py")
#write("( Q_Q)")
#os.system("python3 /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/1602.py")
#time.sleep(5)
print("Loading")
import time
#time.sleep(13)
#import state
#import view
#import os
import random
import requests
#import time
#print(view.state)
#mylcd.lcd_display_string("LOADING LCD",1,0)
mylcd=pwnagotchi.ui.driver.lcd()
name1 = "null"
face = "null1"
url =  "http://127.0.0.1:8666/api/v1/mesh/data"
headers = {}
payload = {}
response = requests.request("GET", url, headers=headers, data = payload)
data = response.json()

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
    time.sleep(random.randint(5,10))
    alert = 0
   #  print("wrote")
 #   os.system("python3 /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/driver.py")
    #write("( Q_Q)")
  #  os.system("python3 /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/1602.py")
#    time.sleep(1)
#    mylcd.lcd_clear()
   # print("(LCD) Attempting to send data to 1602 display")
 #   time.sleep(random.randint(1,3))
 #   mylcd.lcd_display_string("              _ ",1,0)
   # os.system("python3 /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/1602.py")
 #   mylcd.lcd_display_string("              _ ",2,0)
   # refresh()
    try:
         with open(r'/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/myfile.txt', 'r') as file:
          content = file.read()
          if 'busy' in content:
             print("display is busy")
#             exit()
             alert = 1
             time.sleep(10)
#             raise Exception("DISPLAY BUSY")
          else:
             pass
             print("no")
#    time.sleep(10)
         with open('/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/myfile.txt', 'w') as f:
            f.write('busy')
#  
       #  os.system("python3 /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/1602.py")
    #     time.sleep(random.randint(1,3))
         #        print(data) 

         if(alert == 0):
           part = 2
           #name1 = data["name"]
           hor = 5
           name = "pwnagotchi"
           face = "( Q_Q)"
           # face = data["face"]
           #print(face)
           mylcd.lcd_clear()
           mylcd.backlight(0)
           time.sleep(0.1)
           mylcd.backlight(1)

           mylcd.lcd_display_string("              _ ",1,0)
           mylcd.lcd_display_string("              _ ",2,0)
           refresh()
           print(string)
           url =  "http://127.0.0.1:8666/api/v1/mesh/data"
           headers = {}
           payload = {}
           response = requests.request("GET", url, headers=headers, data = payload)
           data = response.json()
 #        print(data)
           part = 2
           name1 = data["name"]
           hor = 5
           face = data["face"]
  #       print(data)
         # write(str(data['face']))
           mylcd.lcd_display_string(face+"                        ",2,16-len(face))
           mylcd.lcd_display_string(name1+"                        ",1,0)
         else:
            print("P")
    except Exception:
         if(alert == 1):
            print("LCD BUSY!")
         else:
            print("LCD Face print failed")
            pass
        # else:

   # time.sleep(random.randint(1,3))
    hor = 15
#    write(str(random.randint(1,9)))
    part = 1
    inp = string
    length = len(inp)
#    refresh()
#    time.sleep(5)
    main = -1
    if length>15 and alert == 0:
#        print("WO")
        for i in range(length+2):
            time.sleep(0.1)
            #print(inp[main:length])
            main = main+ 1
            mylcd.lcd_display_string(inp[main:length]+" "+" ",1,0)
#            print("GOING")
           # time.sleep(0.5)
    elif alert ==0:
          mylcd.lcd_display_string(inp+" "+" ",1,0)
    else:
        print("sk")
    with open('/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/myfile.txt', 'w') as f:
        f.write('ok')
#
part = 1
#refresh()
#print(face)
#write(name1)
#write(face)
#facel = len(face)
#mylcd.lcd_display_string(name1,1,0)
#mylcd.lcd_display_string(face,2,16-len(face))

#write1("dddddddddddddddddddddddddddddddd")
#write1("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
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

