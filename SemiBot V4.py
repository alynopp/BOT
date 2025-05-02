# Bariton altoclef gist (https://github.com/MiranCZ/altoclef/tree/0.18.4), for Fabric 1.21
import random
import time

def sendchat(message): #make this accually send a message in chat and make sure to fix all embadded stuff like with () and "", ''
  print("send command:")
  print(message)
  print(" ")
def wait_until(something):
  # ofc this will not work in python but youll make all code work this is just for easir represintation. in the code you use for the minecraft
  print("waiting...")
  print(" ")
sendchat("#settings LegitMine false")
sendchat("#mine oak_log 5")
wait_until("got 5 > logs in inventory.") # idk like check inv, and when this is in place dont continue until its done like dont sendchat("@get wooden_pickaxe") until thhis is done and continue after, basically add wait until.
time.sleep(1)
sendchat("@get iron_pickaxe")
wait_until("have iron_pickaxe in inv.") #just check if inv have item ykyk like always
sendchat("#mine iron_ore 5")
wait_until("done or have iron ore &, also im using Bariton altoclef gist btw, basically adds auto crafting to bariton. via @get")
sendchat("@get iron_sword")
wait_until("have iron sword")


# make this a loop and when a task is complete it will restart from the loops start / rolls dice again and pick what to do, etc
def mine(item, ammount):
    print("#mine", ammount, item) # make this also send in chat and make sure it sends this and remove stuff like (), , ,'', ('#mine', 'cobblestone', 59)   ---->  #mine cobblestone 59
    print(" ")
    wait_until("action dont, for now there is only a few things that can use this so make it simple just wait until inv have ammount of item, also bartion does not know diff between old items and new ones so there will be a auto stop when inv havehas all the items needed like needs 30 iron and had 30 iron before command it will say done becaouse 30 iron already in inventory.")
rng = random.randint(1, 3)
print("rng: ", rng)
print(" ")
if rng == 1:
  print("exploring...")
  sendchat("#explore")
  time.sleep(20) # keep in the wait cus we want to explore for this long
  sendchat("#stop")
if rng == 2:
  print("minning...")
  print("-->")
  minewat = random.randint(1, 3)
  if minewat == 1:
    print("minning stone")
    mineammount = random.randint(1, 100)
    mine(mineammount, "stone")
  if minewat == 2:
    print("minning coal")
    mineammount = random.randint(1, 15)
    mine(mineammount, "coal_ore")
  if minewat == 3:
    print("minning iron")
    mineammount = random.randint(1, 5)
    mine(mineammount, "iron_ore")
if rng == 3: # does something fun or outstanding
  print("(rng 3):  does minor/fun stuff...") # not acually typing if i ever use print its just for debug and stuff yk.
  print(" ")
  fun = random.randint(1, 2)
  if fun == 1:
    print("(1): getting food...")
    print(" ")
    sendchat("@get beef 4")
    wait_until("have 4 > beef in inv.")
  if fun == 2:
    print("going to nearest surface / any block on top")
    print(" ")
    sendchat("#surface") # since its hard to tell when command is done give it 34 seconds of running and stop it via #stop, then yk reset the loop
    print(" ")


# this is a demo verstion of this bot, also fix some things, i did not add wait_untill in a few places i think idk.
