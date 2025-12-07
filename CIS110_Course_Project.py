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
