# pwnagotchi1602display

PLEASE VIEW THIS IN RAW              
Last tested on 1.5.3

go to /usr/local/lib/python3.7/dist-packages/pwnagotchi
delete that voice.py and replace it with this voice.py
go to /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui
add the remaining files there
go to /etc/pwnagotchi
add 

ui.faces.look_r = "( Q_Q)"
ui.faces.look_l = "(Q_Q )"
ui.faces.look_r_happy = "( ^_^)"
ui.faces.look_l_happy = "(^_^ )"
ui.faces.sleep = "(z_z )"
ui.faces.sleep2 = "( z_z)"
ui.faces.awake = "( Q_Q)"
ui.faces.bored = "(-_-)"
ui.faces.intense = "('Q_Q)"
ui.faces.cool = "(⌐0_0)"
ui.faces.happy = "( ^_^)"
ui.faces.excited = "( ^_^)"
ui.faces.grateful = "( ^_^)"
ui.faces.motivated = "( -_+)"
ui.faces.demotivated = "('-_-)"
ui.faces.smart = "( +_+)"
ui.faces.lonely = "( U_U)"
ui.faces.sad = "( U_U)"
ui.faces.angry = "(-_-')"
ui.faces.friend = "( OwO)"
ui.faces.broken = "( X_X)"
ui.faces.debug = "( #_#)"


to config.toml and make sure to delete the default faces
reboot
