import time # time.sleep(0)
import random

print("started.")
def sendchat(command):
  print("command sent:")
  print(command)
  print(" ")

#### saved locations:
spawnx = 0
spawny = 0
spawnz = 0
homex = 0
homey = 0
homez = 0
####################.
#### Bot inventory:
log = 0
###################
# java & fabric stuff: (some stuff can also be one server join dont limit your self to anything.)
ingame_coordinates = "?, make this update in a loop, the xyz of the bot(real time of idk just make it update. and you can add new veriables for eatch x/y/z this is just for demo.)"
xpos = ingame_coordinates
ypox = ingame_coordinates
zpos = ingame_coordinates
####################.

# on server/lan join:
sendchat("#mine oak_log")
while True:
  if log < 5:
    sendchat("#mine oak_log")
    time.sleep(5)
    log = log +3
    print(log)
  elif log > 4:
    break
#

#test:
print("loop broken")
print(" ")
sendchat("got wood") #normal chat say not command sould work.
#



# #goal command in Baritone.
def goal(x,y,z):
  print("new location goal:")
  print(x,y,z)

goal(1,2,3)
