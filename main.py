##This game is an attemepted remake of the game Wordle found at https://www.nytimes.com/games/wordle/index.html

import os
import sys
from random import randint

low = open('words.txt').read().split('\n')
answer = low[randint(0,662)]
def split(word):
    return [char for char in word]
     

word = answer
word = split(word)

## Borrowed from https://www.codegrepper.com/code-examples/python/how+to+change+the+color+of+the+text+in+python
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  

def start():
  print("WORDLE")
  print("Welcome to Wordle entirely made in python")
  print('-----------------------------------------')
  print("Work to guess the 5 letter word")
  print('-----------------------------------------')
  print(colored(255, 255, 0, "Yellow") + "means the letter is in the wrong spot")
  print('-----------------------------------------')
  print(colored(50, 205, 50, "Green") + "means the letter is in the correct spot")
  print('-----------------------------------------')
  print(colored(128, 128, 128, "Grey") + "means the letter is wrong")
  print('-----------------------------------------')
  print(colored(255, 0, 0,"DO NOT USE CAPITALS "))
  print(colored(50, 205, 50, "Good Luck!"))      

wordright = False
gameover = 0

##print(word)


def game():
  print("You Win The Word Was " + answer)
  playagain()
  
def gamelose():
  print("Sorry You Lost The Word Was " + answer)
  playagain()

def playagain():
  again = input("Would You Like To Play Again? Yes or No?  ")
  if(again == "yes" or again == "Yes"):
    ##Might Not Work on Windows code is for Mac and Linux
    os.system('clear')
    ## Restart Code borrowed from https://www.codegrepper.com/code-examples/python/restart+script+python
    os.execl(sys.executable, sys.executable, *sys.argv)
    start()
  if(again == "no" or again == "No"):
    print("Thank You For Playing")
    exit()

  
start()

while gameover != 6:

  
  guess1 = input("Please Enter Your Guess: ")
  guess1 = split(guess1)


  spot1 = word[0]
  spot2 = word[1]
  spot3 = word[2]
  spot4 = word[3]
  spot5 = word[4]

  answer1 = guess1[0]
  answer2 = guess1[1]
  answer3 = guess1[2]
  answer4 = guess1[3]
  answer5 = guess1[4]

  a = 0
  b = 0
  c = 0

  d = 0
  e = 0
  f = 0

  g = 0
  h = 0
  i = 0

  j = 0
  k = 0
  l = 0

  m = 0
  n = 0
  p = 0

  right1 = 0
  right2 = 0
  right3 = 0
  right4 = 0
  right5 = 0




##Letter 1
  if(answer1 == spot1):
    answer1 == colored(50, 205, 50, answer1)
    a = 0
    b = 205
    c =50
    right1 = 1
  elif(answer1 == spot2 or answer1 == spot3 or answer1 == spot4 or answer1 == spot5):
    answer1 == colored(255, 255, 0, answer1)
    a = 255
    b = 255
    c = 0
  elif(answer1 != spot1 or answer1 != spot2 or answer1 != spot3 or answer1 != spot4 or answer1 != spot5):
    answer1 == colored(128, 128, 128, answer1)
    a = 128
    b = 128
    c = 128

##Letter 2
  if(answer2 == spot2):
    answer2 == colored(50, 205, 50, answer2)
    d = 0
    e = 205
    f =50
    right2 = 1
  elif(answer2 == spot1 or answer2 == spot3 or answer2 == spot4 or answer2 == spot5):
    answer2 == colored(255, 255, 0, answer2)
    d = 255
    e = 255
    f = 0
  elif(answer2 != spot1 or answer1 != spot2 or answer2 != spot3 or answer2 != spot4 or answer2 != spot5):
    answer2 == colored(128, 128, 128, answer2)
    d = 128
    e = 128
    f = 128

##Letter 3
  if(answer3 == spot3):
    answer3 == colored(50, 205, 50, answer3)
    g = 0
    h = 205
    i =50
    right3 = 1
  elif(answer3 == spot1 or answer3 == spot2 or answer3 == spot4 or answer3 == spot5):
    answer3 == colored(255, 255, 0, answer3)
    g = 255
    h = 255
    i = 0
  elif(answer3 != spot1 or answer3 != spot2 or answer3 != spot3 or answer3 != spot4 or answer3 != spot5):
    answer3 == colored(128, 128, 128, answer3)
    g = 128
    h = 128
    i = 128

##Letter 4
  if(answer4 == spot4):
    answer4 == colored(50, 205, 50, answer4)
    j = 0
    k = 205
    l =50
    right4 = 1
  elif(answer4 == spot1 or answer4 == spot2 or answer4 == spot3 or answer4 == spot5):
    answer4 == colored(255, 255, 0, answer4)
    j = 255
    k = 255
    l = 0
  elif(answer4 != spot1 or answer4 != spot2 or answer4 != spot3 or answer4 != spot4 or answer4 != spot5):
    answer4 == colored(128, 128, 128, answer4)
    j = 128
    k = 128
    l = 128

 ##Letter 5
  if(answer5 == spot5):
    answer5 == colored(50, 205, 50, answer5)
    m = 0
    n = 205
    p =50
    right5 = 1
  elif(answer5 == spot1 or answer5 == spot2 or answer5 == spot3 or answer5 == spot4):
    answer5 == colored(255, 255, 0, answer5)
    m = 255
    n = 255
    p = 0
  elif(answer5 != spot1 or answer5 != spot2 or answer5 != spot3 or answer5 != spot4 or answer5 != spot5):
    answer5 == colored(128, 128, 128, answer5)
    m = 128
    n = 128
    p = 128

  
  print("+-+-+-+-+-+-+-+-+-+-+")
  print("| " + (colored(a, b, c, answer1)) + "| " + (colored(d, e, f, answer2)) + "| " + (colored(g, h, i, answer3)) + "| " + (colored(j, k, l, answer4)) + "| " + (colored(m, n, p, answer5)) + "|")
  print("+-+-+-+-+-+-+-+-+-+-+")

  gameover = gameover + 1

  
  
  if(right1 == 1 and right2 == 1 and right3 == 1 and right4 == 1 and right5 == 1):
    gameover = 6
    game()

  elif(gameover == 6):
    gamelose()

