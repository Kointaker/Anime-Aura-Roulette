# Necessary Imports: 
from colorama import Fore
import os
import random
import sys
import time
from Auras import Common, Impossible, Legendary, Master, Rare
from Admin_Key import user_main
from tqdm import tqdm

# Version 5.0 Beta
# Current Goals for 6.0:
    #-Start Balancing:
      #-Advancement (Requirements before some options can be unlocked)
      #-Limit for rolling and x amount of times:
        #-A limit as to how much auras are roll  ed
        #-A limit as to how much this method can be used
    #-Fix Tutorial
  

# Pre-code initializers:
inventory = []
speed = 200




# Roll Functions and Mechanic Functions:
# class Roll_Mechanics():
  

def roll():
  decider = random.randint(1, 1000000)


  if decider <= 100:
    return [random.choice(Impossible), "Red"]
  elif decider <= 1000:
    return [random.choice(Master), "Magenta"]
  elif decider <= 10000:
    return [random.choice(Legendary), "Yellow"]
  elif decider <= 500000:
    return [random.choice(Rare), "LightMagenta"]
  else:
    return [random.choice(Common), "Green"]

    
def no_Master_or_Impossible_roll():
  decider = random.randint(1, 1000)
  if decider <= 5:
    return [random.choice(Legendary), "Yellow"]
  elif decider <= 500:
    return [random.choice(Rare), "LightMagenta"]
  elif decider <= 1000:
    return [random.choice(Common), "Green"]


def multi_roll(user):
  for i in range(user):
    current_aura = no_Master_or_Impossible_roll()
    paint(current_aura)
    inventory.append(current_aura[1])
    print(current_aura[0])


def super_roll():
  decider = random.randint(1, 1000000)
  if decider <= 1000:

    return [random.choice(Impossible), "Red"]
  elif decider <= 10000:
    limit -= 1
    return [random.choice(Master), "Magenta"]
  elif decider <= 100000:
    limit -= 1
    return [random.choice(Legendary), "Yellow"]
  elif decider <= 1000000:
    limit -= 1
    return [random.choice(Rare), "LightMagenta"]
  else:
    return print("You have no more super rolls left.")

def admin_roll():
  decider = random.randint(1, 10)
  if decider <= 1:
    return [random.choice(Impossible), "Red"]
  elif decider <= 3:
    return [random.choice(Master), "Magenta"]
  elif decider <= 10:
    return [random.choice(Legendary), "Yellow"]


def admin_multi_roll(admin_choice):
  for i in range(admin_choice):
    current_aura = admin_roll()
    paint(current_aura)
    inventory.append(current_aura[1])
    print(current_aura[0])


# Typing speeds
def medium_type(t, speed):
  typing_speed = speed #wpm
  for l in t:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(random.random()*10.0/typing_speed)
  print('')


def tutorial(tut):
  if tut == "n":
    return
  if tut == "y":
    speed = 200
    print("\n\nTutorial: \n")
    t = "Welcome to the Dragon Ball Form Roulette\nWhere you roll for auras from the Dragon Ball Franchise."
    medium_type(t, speed)
    xn = input("\n\n===Press Enter to continue===\n>>>")
    if xn != "":
        sys.exit()
    t = "\nYou can collect these auras and view which ones your missing.\nUse a variety of roll methods to collect a variety of rarities"
    medium_type(t, speed)
    xn = input("\n\n===Press Enter to continue===\n>>>")
    if xn != "":
        sys.exit()
    t = f"\nWhenever this pops up: {Fore.RED}===Press Enter to continue==={Fore.RESET}:\nYou can press enter to continue the program, or input any other key to cancel the program. \nTry it down below!"
    medium_type(t, speed)
    xn = input("\n\n===Press Enter to continue===\n>>>")
    if xn != "":
        print("Exactly like that!")
        time.sleep(1)
        t = "What you just did will exit the program, as said before."
        medium_type(t, speed)
        xn = input("\n\n===Press Enter to continue===\n>>>")
        if xn != "":
            sys.exit()
    else:
      print("Woah, remember, this is to continue the game. you can exit the program at any time as said before.")
      xn = input("\n\n===Press Enter to continue===\n>>>")
      if xn != "":
          sys.exit()
    t = "\nSome options are locked behind a requirement.\nPass this requirement to be able to use these options."
    medium_type(t, speed)
    xn = input("\n\n===Press Enter to continue===\n>>>")
    if xn != "":
        sys.exit()
    t = "\nUse the See Auras option to look at all the games auras, as well \nas the auras you have obtained."
    medium_type(t, speed)
    xn = input("\n\n===Press Enter to continue===\n>>>")
    if xn != "":
        sys.exit()
    t = "\nWarning: Make sure to input your options correctly.\nThis is because the Dragon Ball Form Roulette is in Beta mode, \nand some input safety measures are not currently in place."
    medium_type(t, speed)
    xn = input("\n\n===Press Enter to continue===\n>>>")
    if xn != "":
        sys.exit()
    t = "\nPlease treat this game with care, and enjoy!"
    medium_type(t, speed)
    xn = input("\n\n===Press Enter to finish the Tutorial===\n>>>")
    if xn != "":
        sys.exit()
  

  else:
    print("Invalid Input: Tutorial canceled")
    time.sleep(1)


# Color Coding
def paint(current_aura):
  if current_aura[1] == "Red":
    current_aura[1] = current_aura[0]
    current_aura[0] = f"{Fore.RED}{current_aura[0]}{Fore.RESET}"
  
  if current_aura[1] == "Magenta":
    current_aura[1] = current_aura[0]
    current_aura[0] = f"{Fore.MAGENTA}{current_aura[0]}{Fore.RESET}"
  
  if current_aura[1] == "Yellow":
    current_aura[1] = current_aura[0]
    current_aura[0] = f"{Fore.YELLOW}{current_aura[0]}{Fore.RESET}"
  
  if current_aura[1] == "LightMagenta":
    current_aura[1] = current_aura[0]
    current_aura[0] = f"{Fore.LIGHTMAGENTA_EX}{current_aura[0]}{Fore.RESET}"
  
  if current_aura[1] == "Green":
    current_aura[1] = current_aura[0]
    current_aura[0] = f"{Fore.GREEN}{current_aura[0]}{Fore.RESET}"




# Initial Load animation (1 time)
for i in tqdm (range (250), 
               desc="Booting", 
               ascii=False, ncols=75):\
  time.sleep(0.0029)

print("Complete.")


# Choice for tutorial
tut = input("Would you like to see the tutorial? (y/n): ").lower()

#Either starts tutorial, or skips and goes to game
tutorial(tut)


# Code loop
# Loops until the user quits

while True:
  
  # Start of Game
  print(f"\n\n\n\033[1m{Fore.RED}==========Dragon Ball Form Roulette=========={Fore.WHITE}\033[0m\n\n")


  time.sleep(1)
  

  # User options
  print("""        Would you like to:""")
  t = f"""
        
                          Not Implemented:
                          2. Do a super roll; Chances:
                              {Fore.GREEN}Common-0%
                              {Fore.LIGHTMAGENTA_EX}Rare-90%
                              {Fore.YELLOW}Legendary-10%
                              {Fore.MAGENTA}Master-1%
                              {Fore.RED}Impossible-0.1%{Fore.RESET}
                          
        
        
        1. Do a normal roll; Chances:
            {Fore.GREEN}Common-Almost guaranteed
            {Fore.LIGHTMAGENTA_EX}Rare-50%
            {Fore.YELLOW}Legendary-1%
            {Fore.MAGENTA}Master-0.1%
            {Fore.RED}Impossible-0.01%{Fore.RESET}
        
        
        3. (Normal) Roll until you get {Fore.YELLOW}Legendary{Fore.RESET} or higher
            Estimated time: ~1 minute
        4. (Normal) Roll until you get {Fore.MAGENTA}Master{Fore.RESET} or higher
            Estimated time: ~10 minutes
        5. (Normal) Roll until you get {Fore.RED}Impossible{Fore.RESET}
            Estimated time: ~30 minutes
        6. Roll an x amount of times:
            -{Fore.MAGENTA}Master{Fore.RESET} and {Fore.RED}Impossible{Fore.RESET} are unobtainable here
            -{Fore.YELLOW}Legendary{Fore.RESET} rates are halved ({Fore.YELLOW}0.5%{Fore.RESET})


        
        7. Admin Control Panel
        8. See Auras
        9. Review the tutorial
        10. Exit
"""
  speed = 90000
  medium_type(t, speed)
  
  # Option Choice for User
  try:
    user_choice = int(input(">>>"))
  except ValueError:
    print("\nPlease enter a valid number next time")
    time.sleep(1)
    continue

  if user_choice > 11:
    print("Enter a valid number next time")

  
  # User choice pathways:

  
  # Singular Normal Roll
  if user_choice == 1:
    current_aura = roll()
    paint(current_aura)
    print("\nYou rolled and got: \033[1m" + current_aura[0] + "\033[0m")
    inventory.append(current_aura[1])
    xn = input("\n\n===Press Enter to continue===\n>>>")
    if xn != "":
        sys.exit()
    
  
  # Singular Super Roll
  if user_choice == 2:
    current_aura = super_roll(limit)
    print(limit)
    paint(current_aura)
    print("\nYou rolled and got: \033[1m" + current_aura[0] + "\033[0m")
    inventory.append(current_aura[1])
    xn = input("\n\n===Press Enter to continue===\n>>>")
    if xn != "":
        sys.exit()

  # Roll until Legendary or higher
  if user_choice == 3:
    gained = True
    while gained == True:
      current_aura = roll()
      paint(current_aura)
      # print(current_aura)
      if current_aura[1] in Legendary:
        print("Your 1/100 Legendary is: \033[1m", end="")
        paint(current_aura)
        inventory.append(current_aura[1])
        time.sleep(1)
        print(current_aura[0])
        xn = input("\n\n===Press Enter to continue===\n>>>")
        if xn != "":
            sys.exit()
        gained= False
      if current_aura[1] in Master:
        print("your 1/1000 Master is: \033[1m", end="")
        paint(current_aura)
        inventory.append(current_aura[0])
        time.sleep(1)
        print(current_aura[0])
        xn = input("\n\n===Press Enter to continue===\n>>>")
        if xn != "":
            sys.exit()
        gained = False
      if current_aura[1] in Impossible:
        print("Your 1/10000 Impossible is: \033[1m", end="")
        paint(current_aura)
        inventory.append(current_aura[1])
        time.sleep(1)
        print(current_aura[0])
        xn = input("\n\n===Press Enter to continue===\n>>>")
        if xn != "":
            sys.exit()
        gained = False
      print(current_aura[0])
      inventory.append(current_aura[1])
      print("")
      time.sleep(0.07)


  
  # Roll until Master or Higher
  if user_choice == 4:
    gained = True
    while gained == True:
      current_aura = roll()
      paint(current_aura)
      if current_aura[1] in Master:
        print("your 1/1000 Master is: \033[1m", end="")
        inventory.append(current_aura[1])
        time.sleep(1)
        print(current_aura[0])
        xn = input("\n\n===Press Enter to continue===\n>>>")
        if xn != "":
            sys.exit()
        gained = False
      if current_aura[1] in Impossible:
        print(f"Your 1/10000 Impossible is: \033[1m", end="") 
        inventory.append(current_aura[1])
        time.sleep(1)
        print(current_aura[0])
        xn = input("\n\n===Press Enter to continue===\n>>>")
        if xn != "":
            sys.exit()
        gained = False
      else:
        print(current_aura[0])
        inventory.append(current_aura[1])
        print("")
        time.sleep(0.07)

  # Roll until Impossible
  if user_choice == 5:
    gained = True
    while gained == True:
      current_aura = roll()
      paint(current_aura)
      if current_aura[1] in Impossible:
        print("Your 1/10000 Impossible is: \033[1m", end="")
        inventory.append(current_aura[1])
        time.sleep(1)
        print(current_aura[0])      
        xn = input("\n\n===Press Enter to continue===\n>>>")
        if xn != "":
            sys.exit()
        gained = False
      else:
        print(current_aura[0])
        inventory.append(current_aura[1])
        print("")
        time.sleep(0.07)


  
  # Multi Roll x amount of times (Balanced)
  if user_choice == 6:
    user = int(input("How many times?\n>>>"))

    print("\nCollected Auras: \n\n")
    multi_roll(user)
    xn = input("\n\n===Press Enter to continue===\n>>>")
    if xn != "":
        sys.exit("")

      
  # Admin Control Panel
  if user_choice == 7:
    admin_parser = input("Username: \n>>>")
    if admin_parser in user_main["Users"]:
      admin_parser = input("Password: \n>>>")
      if admin_parser in user_main["Passwords"]:
        gained = True
        while gained == True:
          print("\n==Admin Control Panel (ACP)==\n\n\n")
          time.sleep(1)
          print(f"""What would you like to do in the ACP?

          1. Add aura to inventory
          2. Remove aura from inventory
          3. Clear inventory
          4. Use admin roll x amount of times
          5. Add admin user
          6. exit ACP""")
          admin_choice = int(input(">>>"))
          if admin_choice == 1:
            admin_choice = input("What aura would you like to add?\n>>>")
            inventory.append(admin_choice)
            print("\nAura successfully added")
          if admin_choice == 2:
            admin_choice = input("What aura would you like to remove?\n>>>")
            try:
              inventory.remove(admin_choice)
            except ValueError:
              print("\n--Aura not found--")
              continue
            print("\nAura successfully removed")
          if admin_choice == 3:
            inventory.clear()
            print("\nInventory successfully cleared")
          if admin_choice == 4:
            admin_choice = int(input("How many times?\n>>>"))
            print("Collected Auras: ")
            admin_multi_roll(admin_choice)
            xn = input("\n\n===Press Enter to continue===\n>>>")
            if xn != "":
                sys.exit()
          if admin_choice == 5:
            add = input("\nWho would you like to add?\n>>>")
            add2 = input("\nEnter their password\n>>>")
            
            user_main["Users"].append(add)
            user_main["Users"].append(add2)
          if admin_choice == 6:  
            print("\nExiting the ACP...")
            gained = False

  # Display users aura inventory
  if user_choice == 8:
    print("====Inventory====\n\n")
    print("Guide:\nWhite = Not Owned\nColored = Owned\n")
    print(f"\n\033[1m{Fore.GREEN}Common:{Fore.RESET}\033[0m\n")
    for i in range(len(Common)):
      if Common[i] in inventory:
        print(f"{Fore.GREEN}" + Common[i] + f"{Fore.RESET}" + " (Owned)")
      else:
        print(Common[i])
    print(f"\n\n\033[1m{Fore.LIGHTMAGENTA_EX}<Rare>:{Fore.RESET}\033[0m\n")
    for i in range(len(Rare)):
      if Rare[i] in inventory:
        print(f"{Fore.LIGHTMAGENTA_EX}" + Rare[i] + f"{Fore.RESET}" + " (Owned)")
      else:
        print(Rare[i])
    print(f"\n\n\033[1m{Fore.YELLOW}<<Legendary>>:{Fore.RESET}\033[0m\n")
    for i in range(len(Legendary)):
      if Legendary[i] in inventory:
        print(f"{Fore.YELLOW}" + Legendary[i] + f"{Fore.RESET}" + "(Owned)")
      else:
        print(Legendary[i])
    print(f"\n\n\033[1m{Fore.MAGENTA}<<<Master>>>:{Fore.RESET}\033[0m\n")
    for i in range(len(Master)):
      if Master[i] in inventory:
        print(f"{Fore.MAGENTA}" + Master[i] + f"{Fore.RESET}" + " (Owned)")
      else:
        print(Master[i])
    print(f"\n\n\033[1m{Fore.RED}<<<<Impossible>>>>:{Fore.RESET}\033[0m\n")
    for i in range(len(Impossible)):
      if Impossible[i] in inventory:
        print(f"{Fore.RED}" + Impossible[i] + f"{Fore.RESET}" + " (Owned)")
      else:
        print(Impossible[i])

    xn = input("\n\n===Press Enter to continue===\n>>>")
    if xn != "":
      sys.exit()

  # Runs the tutorial
  if user_choice == 9:
    tutorial(tut)
  # Exits the game
  if user_choice == 10:
      print("\nExiting the game...")
      time.sleep(1)
      sys.exit("\n\033[1mTerminated\033[0m")

