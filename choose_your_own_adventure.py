# In this project we will try nesting

name = str(input("Enter Your Name: "))
print(f"\nWelcome {name} to this adventure")

answer = str(input("\nYou are on a dirt road, it has come to an end, go left or right. Which way do you want to go?(left/right): ").lower())

if answer == "left":
    answer = str(input("\nYou come to a river, you can walk around it or swim across? Type Walk to walk around or Swim to swim across: ").lower())
    
    if answer == "swim":
        print("\nYou swam across the river and swallowed by a 22 feet burmese python.")
    elif answer == "walk":
        print("\nYou walked for many miles and found a helicopter with supplies. You WON!")
    else:
        print("\nNot a valid option. You are dead.")

elif answer == "right":
    answer = str(input("\nYou come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back): ").lower())
    
    if answer == "back":
        print("\nYou go back and eaten by a zombie.")
    elif answer == "cross":
        answer = str(input("\nYou cross the bridge and meet a stranger. Will you talk to them?(Yes/No): ").lower())
        if answer == "yes":
            print("\nThey gave you a key of the boat and You WON!")
        elif answer == "no":
            print("\nThe stranger got offended and they handed you to the zombies.")
        else:
            print("\nNot a valid option. You are dead.")
    else:
        print("\nNot a valid option. You are dead.")

else:
    print("Not a valid option. You are dead.")

print(f"Thank you for trying this game {name}.")