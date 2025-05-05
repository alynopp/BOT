# Bariton altoclef gist (https://github.com/MiranCZ/altoclef/tree/0.18.4), for Fabric 1.21
import random
import time

# Functions:
def sendchat(message): #make this accually send a message in chat and make sure to fix all embadded stuff like with () and "", ''
  print("send command:")
  print(message)
  print(" ")
def wait_until(something):
  # ofc this will not work in python but youll make all code work this is just for easir represintation. in the code you use for the minecraft
  print("waiting...")
  print(" ")

# on server join, or idk just make sure they can still use the functions/def's
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
