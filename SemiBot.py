# note turn on legitMine in Baritone.
# https://github.com/cabaletta/baritone/blob/1.19.4/USAGE.md
# 1.20.1 fabric Local-Lan/Server
import time # time.sleep(5)
import random # not used yet.
#make sure the code runs when the bot is in the server so it does not run in the menu.
#print and sendchat are different print is fir consol and debuging sendchat is to controll the bot via Baritone.
# #goto is simple movenmeny, #goal is with path tracing and mining and building to get to goal you can change type if its needed in a place.

# for Baritone basically does everything.
def sendchat(message):
  print("sending chat command")

# small test
time.sleep(0) # make 0 --> 5
sendchat("#click")

#### for python cus i get error cus ingame_xcoordinate does not exist yet:
ingame_xcoordinate =1
ingame_ycoordinate =2
ingame_zcoordinate =3
#### i dont need this its just to avoid errors in python. (ingame_zcoordinate =3)




# location and stuff 
#make the xyz auto update
xpos = ingame_xcoordinate
ypos = ingame_ycoordinate
zpos = ingame_zcoordinate

spawnx = xpos
spawny = ypos
spawnz = zpos

# small debug for test:
print("#goto",spawnx,spawny,spawnz) #make sure that everything always sends without other imperfections like this sends ('#goto', 1, 2, 3) but i need #goto 1 2 3

def goto(x,y,z):
  print(" ")
  print("going to: ")
  print(x,y,z)
  #make this sent chat with Baritone to use #goto x y z   command.

#small test.
goto(spawnx,spawny,spawnz+5)

time.sleep(3)
print(" ")

def ingame_inventory(item):
  print("inv")

#only oak for now.
sendchat("#mine oak_log")
#make this have a java wait until bot was 6 logs in inv / ingame_inventory then send a #stop

# this is a small test vertion and a small practice not full vertion













