import random

#Generate a random no 
number=random.randint(1,100)
attempts = 0


print("Welcome to no guessing game !")


while True:
    guess= int(input("Gusess a no between 1 to 100:"))
    attempts += 1
    
    
    if guess < number:
        print("Too low try again")
        

    elif guess > number:
        print("Too high try again")
    
    
    else:
       print(f"correct! you guessed it in {attempts} attempts ")
       break
    
    
    
        
    
    



