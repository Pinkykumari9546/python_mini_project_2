import random

n = random.randint(1, 100)
a = -1
guesses = 1

print("Guess number between 1 and 100:")
while(a != n):
    
    a = int(input("Enter your guess: "))
    if(a > n):
        print("Lower number please")
        guesses += 1
    elif(a < n):
        print("Higher number Please")
        guesses += 1

print(f"Congratulations! You have guessed the number {n} correctlly in {guesses} attempts")