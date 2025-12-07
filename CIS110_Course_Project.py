print(f"Welcome...")
print(f"I would love to share a story with you about a turtle that needs to make a decision that will shape it's life forever!")
print(f"First, lets get some details from you..")
print(f"Make sure to press 'Enter' after your responses")
input(f"\nPress the enter key to continue...")


color = input("\nWhat is your least favorite secondary color:  ")
while color.lower() not in ["purple", "orange", "green"]:
    color = input("That is not a secondary color, try again:  ")
name = input("\nWhat is the turtle's name :  ")
while len(name) == 0:
    name = input("Please give the turtle a name:  ")
location = input("\nWhat is your dream destination:  ")
while len(location) == 0:
    location = input("Invalid entry! What is your dream destination:  ")
age = input("\nWhat is your favorite number:  ")
while not age.isdigit():
    age = input("Value not understood. Only enter the numeric value:  ")
emotion = input("\nWhat is your current mood:  ")
while emotion.lower() not in ["happy" , "sad" , "angry" , "excited" , "bored" , "mad"] :
    emotion = input("Keep it simple. Are you happy, mad, excited or angry:  ")


print(f"Let us begin")
print(f"\nThere once lived a {color} turtle named {name}. ")
print(f"{name} currently lives at the {location} zoo. ")
print(f"Over the past {age} years {name} has had many fights and arguments with the other turtles. ")
print(f"{name} WANTS OUT! ")
print(f"{name} plans to leave in 15 minutes during the next enclosure cleaning. ")

leavethezoo = input(f"\nDo you think {name} the turtle should leave the {location} Zoo? Type Yes or No:  ")
while leaveThezoo.lower() != "yes" and leaveThezoo() != "no":
    leaveThezoo = input("It is a Yes or No question:  ")


if leaveThezoo.lower() == "yes": 
    print(f"\n{name} makes his BIG break! He makes his way around {location} to check out the view. ")
    print(f"{name} the turtle begins to roam the city and runs into a little {color} compass that points him in the way he plans to go. ")
    print(f" So {name} keep the compass because he felt a connection to it. ")
    print(f"{name} follows the compass and it points towards a waterpark. ")
    print(f"He sees a huge sign that reads {location} WaterParkk! and he heads over. ")

else:
    print(f"\n{name} the turtle decides to stay in the {location} Zoo.")
    print(f" The other turtles begin to gang up on him. {name} is well known in the area and has a bad reputation. ")
    print(f"{name} holds his ground because he no longer wants to be a menace. ")
    print(f"The tutle begins to feel {emotion} and goes off to lay by the pond with the other unmarried turtles. ")


if 


    

