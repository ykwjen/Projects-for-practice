# Hangman

# random word generator
import requests  #after installing requests module through settings
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()
import random
answer = random.choice(WORDS)
answer = bytes.decode(answer, 'utf-8') #convert bytes class type of answer to string
n= 10  #number of times player can make a guess
len = len(answer)
lst = [letter for letter in answer] #make a list with elements of each letter in answer
Hint = []
x = len
while x !=0:          #loop for creating a list for the hint in which number of elements depend on number of letters in answer
    x= x-1
    Hint.append("_")
FirstHint = []
FirstHint.append("_"*len) #lists are mutable but strings are not
strhint = str(Hint)[2:-2]
strfirsthint = str(FirstHint)[2:-2]
print(answer)
print("Hint: "+ strfirsthint)
print(Hint)


#loop of input and hint
LetterGuess = input("Enter a letter to save the man from hanging: ")        #first prompt for user to input
while strhint != answer and n>0:
      n -= 1                              #reduce chance for guessing each time user inputs a letter
      for i in range(len):
            if LetterGuess == answer[i]:
                # print(i)
                Hint[i] = LetterGuess
      strhint = str(Hint)[2:-2]
      strhint = strhint.replace("\'","")  #to make a string comparable with answer without nonsense such as symbols like ", _ or empty space
      strhint = strhint.replace("_","")
      strhint = strhint.replace(",","")
      strhint = strhint.replace(" ", "")
      printhint = str(Hint)[2:-2]
      printhint = printhint.replace("\'","") #to make a string that can be presented to user preserving _ to indicate where the letters are
      printhint = printhint.replace(",","")
      printhint = printhint.replace(" ", "")
      if strhint != answer:
        LetterGuess = input("Remaining chances = "+ str(n) + "\n" + "Hint: "+ printhint + "\n" + "Enter a letter to save the man from hanging: ")    #prompt for user to input if answer is not correct yet
if strhint != answer:
    print("You lost.")
else:
    print("You won!")


