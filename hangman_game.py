import random
    #gives  access to  random functions
import sys
    #gives access to variables and functions which are maintained by interpreter


    #let us create list of words
words_list  =  ["java" , "python" , "programming" , "language" , "computer", "window" , "software" , "laptop" , "processor" , "compiler" , "interpeter" , "mouse"  ]

letter_storage = []    # to store letters enterd by user

alphabet = "abcdefghijklmnopqrstuvwxyz"

list = []



def introducing():
    print("\nHello friend")

    while True:

        name = input("Please enter your name : ")

        if name == "":
            print("you can't do that! no blank lines")

        else:
            break
    print( "\nWell ! Do you want to play game with me")
    while True:
        game_interest = input("Type : yes or no\n").upper()
        if game_interest == "YES" or game_interest == "Y":
            break
        elif game_interest == "NO" or game_interest == "N":
            sys.exit("ok bye ! have a nice day")
        else:
            print("please answer only YES or NO")
            continue
         
introducing()

print("\nThe game is about a  word selected by the  computer and you have to guess it within  5 attempts\n")
print("..............RULES................")   
print("-> you have only 5 chances to guess the word")
print("-> Remember you can enter only 1 letter at a time")
print("-> Maxmimum score you can get is 100")
print("-> If you failed to guess the word you will be awarded 0")
print("-> For every wrong letter you entered marks will be reduced by 20 points and your chances will also decrease by 1\n")

def change_word(secret_word):
    length_of_word = len(secret_word)  # to find length of secret word
    guess_word = []  # to hide the secret word
    for character in secret_word:
        guess_word.append("-")
     

    print("Game begins:\n")
    print("The word you need to guess has",length_of_word, "letters")
    print(guess_word)
    guessing(guess_word,secret_word,length_of_word)


def guessing(guess_word,secret_word,length_of_word):
    i = 100
    guess_taken = 1
    letter_storage = []

    while guess_taken <= 5:
          guess = input("Enter a letter\n").lower()
          if len(guess) > 1:
              print ("You can enter only one letter at a time")
          elif not guess in alphabet :         # checking point
              print ( " Enter only alphabets")
          elif guess in letter_storage:       #checking if letter has been already entered
              print("You have already guessed that letter :-)")
          else:
              letter_storage.append(guess)
              if guess in secret_word:
                  print("you guessed correctly :-)")
                  for x in range(0,length_of_word):
                  # this is to fill blank in the word if correct letter is guessed
                      if secret_word[x] == guess:
                         guess_word[x] = guess
                         print(guess_word)
                  if not '-' in guess_word:
                      print("\nhuhu you won")
                      print("score =",i)
                      if i == 100:
                         print("You are at first position")
                         list.append("first position")
                      elif i == 80:
                         print("You are at second position")
                         list.append("second position")
                      elif i == 60:
                         print("You are at third position")
                         list.append("third position")
                      elif i == 40:
                         print("You are at fouth position")
                         list.append("fourth position")
                      elif i == 20:
                         print("You are at last but one position")
                         list.append("last but one position")
                      break
              else:
                  print("The letter is not in the word. Try Again!")
                  guess_taken += 1
                  i = i - 20
                  if guess_taken == 6:
                      print("sorry friend , you lost :<! The word given to you is",secret_word,"\n")
                      print("score=",i)
                      print ("You are at last position")
                      list.append("last position")
while True:                      
    next = input("\nTpye 'continue' if wou wanna play  or 'exit' if you wanna quit : ").lower()
    if next == "continue":
       secret_word = random.choice(words_list) # to select a word randomly from list
       change_word(secret_word) # calling function to change secret word
    elif next == "exit":
       print("Review of all your games")
       print(list)
       print("Game over")
       sys.exit("Have a nice day")

                     

    


