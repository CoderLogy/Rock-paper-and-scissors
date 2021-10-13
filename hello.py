import random
cat = input("Please enter your result rock,paper or scissors: ")
dog = ["rock","paper","scissors"]
me = random.choice(dog)
print(f"\nYou chose {cat}, computer chose {me}.\n")
if cat == me:
    print("No one is winner in such dawn ages")
elif cat == "rock":
        if me == "scissors":
            print("Rock break scissors you win")
        else:
            print("You loose pc has a big paper that covers you")
elif cat == "paper":
        if me == "scissors":
            print("Bro pc wins, scrissors cut paper")
        else:
            print("You win freak paper cover rock")
elif cat == "scissors":
        if me == "paper":
            print("Slow scissors cuts paper")
        else:
            print("Scissors is destroyes by rock")
else:
    raise Exception("Somthing gone wrong, fixing it try again:")
            