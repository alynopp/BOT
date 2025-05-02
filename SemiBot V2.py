import time
import random
# Bariton altoclef gist (https://github.com/MiranCZ/altoclef/tree/0.18.4), for Fabric 1.21
def sendchat(message):
  print("sent command:")
  print(message)
  print(" ")

sendchat("#settings Legitmine false") # spell check
inv = 0 #just check if inv have item

sendchat("#mine oak_log 5") 
#add wait until, until inv have at least 5 oak_logs

#after until 5 logs:
sendchat("@get crafting_table")
#wait until inv have crafting table, then:
sendchat("@get stick 5")
time.sleep(4)
sendchat("@get wooden_pickaxe")
#wait until inv have wooden_pickaxe
sendchat("#explore")
time.sleep(30)
#build schematic of simple wooden house using schemakic place and auto build make sure player not in water else #explore for another 8 and repeat yk.
#after house build idk how to check like run #pregress or #tasks and check for chat response and wait until, until home/schematic is done being built:
ingame_x = 1 # make real ingame cords and update frequantly or a loop.
ingame_y = 2 # make real ingame cords and update frequantly or a loop.
ingame_z = 3 # make real ingame cords and update frequantly or a loop.
homex = ingame_x
homey = ingame_y
homez = ingame_z

sendchat("#goto white_bed") # fix maybe incorrect format
time.sleep(2)
sendchat("@bed")

rnd1 = random.randint(1, 3)
#rnd1 = 1: explore
#rnd1 = 2: mine
#rnd1 = 3: 
# maket this a loop thingy yk when one task is done the dice is thrown again:

if rnd1 ==1:
  print("exploring...")
  print(" ")
  sendchat("#explore")
if rnd1 ==2:
  print("mining...")
  print(" ")
  minewat = random.randint(1, 4)
  if minewat == 1:
    print("minning cobblestone...") # spell check
    mineammount = random.randint(1, 100)
    print(" ")
    sendchat("#mine cobblestone", mineammount) #fix this and any other code with this problem so all sendchat commands send in the correct format not ('#mine cobblestone', 82) but #mine cobblestone 64
  if minewat == 2:
    print("mining coal...")
    mineammount = random.randint(1, 12)
    print(" ")
    sendchat("#mine coal_ore", mineammount) #fix this and any other code with this problem so all sendchat commands send in the correct format not ('#mine cobblestone', 82) but #mine cobblestone 64
  if minewat == 3:
    print("minning iron...")
    mineammount = random.randint(1, 20)
    print(" ")
    sendchat("#mine coal_ore", mineammount) #fix this and any other code with this problem so all sendchat commands send in the correct format not ('#mine cobblestone', 82) but #mine cobblestone 64
  
