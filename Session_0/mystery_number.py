"""
Build a number guessing game where there is 
a target number the user must find it, when 
the user enter a number, you must indicate if 
the desired one is less or more than the input, 
the user has 10 attempts, if he did not find 
the number within those attempts, he loses, 
if he finds it he wins, you should put that in 
a function. Note: you can use the library random 
to generate the target number or you can simply 
put it manually in your code. 
"""


import random



def win():
  print("you won !")
  return True
  
def try_again(guess, lives):
  hint = "smaller" if guess > mystery_num else "bigger"
  print("try a "+hint+" number, you have ", lives, " lives left")
  return False

def lose(mystery_num):
  print("binary search didn't work ?\nthe mystery number was ",
  mystery_num, "\n")
  return False


# game main function
def guess_mystnum(mystery_num, lives):
  guess = int(input())

  if guess == mystery_num:
    return win()
  elif lives > 1:
    return try_again(guess, lives-1)
  else:
    return lose(mystery_num)


print("""A salamo 3alaycom and wellcom to 
Guess The Mystery Number !\n""")

exit_game = False

# game loop
while (exit_game == False):
  mystery_num = random.randint(0, 2048)
  print (mystery_num)
  lives = 10
  print("the random number is between 0 and 2047\nyou have ",
  lives, " lives\n")

  while (lives > 0):
    if guess_mystnum(mystery_num, lives):
      break
    else:
      lives-=1
  
  print("do you want to reply ? (Y): yes, (N): no")
  if input() != "Y":
    print("Salam alicom")
    exit()
  else:
    print("let' go !\n\n")
