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


leaveThezoo = input("Do you think the turtle should leave the Zoo? Type Yes or No:  ")

while leaveThezoo.lower() != "yes" and leaveThezoo.lower() != "no":
    print("Please enter Yes or No")
    leaveThezoo = input("It is a Yes or No question:  ")


if leaveThezoo.lower() == "yes": 
    print(f"\n{name} makes his BIG break! He makes his way around {location} to check out the view. ")
    print(f"{name} the turtle begins to roam the city and runs into a little {color} compass that points him in the way he plans to go. ")
    print(f" So {name} keep the compass because he felt a connection to it. ")
    print(f"{name} follows the compass and it points towards a waterpark. ")
    print(f"He sees a huge sign that reads {location} WaterPark! and he heads over. ")

else:
    print(f"\n{name} the turtle decides to stay in the {location} Zoo.")
    print(f" The other turtles begin to gang up on him. {name} is well known in the area and has a bad reputation. ")
    print(f"{name} holds his ground because he no longer wants to be a menace. ")
    print(f"The tutle begins to feel {emotion} and goes off to lay by the pond with the other unmarried turtles. ")

print(f"While relaxing and roaming {name} the {color} turtle feels like continuing the journey. ")
print(f"It is time to make the next choice. ")

turtleNewlife = input("Should the turtle begin to fix his reputation? Type Yes or No:  ")

while turtleNewlife.lower() != "yes" and turtleNewlife.lower() != "no":
    print("Please just answer Yes or No")
    turtleNewlife = input(f"It is a Yes or No question:  ")


if turtleNewlife.lower() == "yes":
    print(f"\n{name} the turtle thinks its better off to be the bigger turtle. ")
    print(f"{name} decides to do {age} laps around the entire zoo every day for the next 100 days. ")
    print(f"After this time is up {name} finds his inner self and becomes the nicest turtle in entire {location} zoo. ")
    print(f"{name} begins to be kind to others and brings joy into the other turtles lives. ")


else:
    print(f"\n{name} remains in the {emotion} state and continues to be a menace in other turtles lifes. ")
    print(f"He end up sad and alone no one want to play with him or speak to him. ")
    print(f"The turtle spends another {age} years in the {location} Zoo and dies and never finds a spouse. ")

if leaveThezoo.lower() == "yes" and turtleNewlife.lower() == "yes":
    print(f"\n{name} fixes his life. ")
    print(f"He ends up finding a wife and has {age} baby turtles. ")
    print(f"{name} The Turtle Lives Happily Ever After! ")
elif leaveThezoo.lower() == "no" and turtleNewlife.lower() == "no":
    print(f"\n{name} the turtle never fixes his life. ")
    print(f"The turtle got stuck in the {emotion} and never saw past it. ")
    print(f"{name} ends up losing his vibrant {color} color and withers away. ")
else:
    print(f"\nAfter enjoying his time in {location} the turtle decides to carry on. ")
    print(f"He's tired of the way his life has been going and just wants to feel {color} and {emotion} again. ")
    print(f"Another {age} years go by and now is up in age. ")
    print(f"{name} the Great Turtle looks back over his life and feels {emotion} about all of the choices he had to make. ")
    print(f"\nThe END!")

keepGoing = input(f"\nWould you like another story? Enter yes or no:  ")
while keepGoing.lower() != "yes" and keepGoing.lower() != "no":
    keepGoing = input(f"Invalid! Enter yes or no:  ")












    

