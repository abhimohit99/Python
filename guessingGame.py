import random
rand = random.randint(1,1000)

print("Rules: guess between 1 and 1000. Have fun!")

guesses = [0] #going to save guesses in a list

while True:
    guess = int(input("Guess: "))
    guesses.append(guess)
    
    if(guess <= 0 or guess > 100):
        print("Input a number between 1 and 100.")
        continue
    
    diff = abs(rand-guesses[-2]) #difference between the random number and the previous guess
    diff1 = abs(rand-guess) #difference between the random number and the current guess
    
    if (guess == rand):
        print("Corret! You win!")
        break
    
    if (guesses[-2] == 0): #this block is for the case when there has only been 1 guess made, so no "previous" guess is there.
        if(abs(guess-rand)<10):
            print("WARM")
        else:
            print("COLD")
    
    elif(diff1 < diff): #if user's guess is closer than before
        print("Warmer")
    
    elif(diff1 > diff): #if the guess is further away
        print("Colder...")
    
    else: #if the same number is put in consecutively
        print("The same number won't magically work this time...")
