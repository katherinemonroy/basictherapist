name = input("What is your name? ") # asks and then stores what you input as your name into the variable "name"

mood = int(input("rate your day 1-10: ")) # asks and stores your input into "mood"

if mood < 5: # if mood is less than a 5
    rant = input("What made it a not-so-good day? ") # allows for you to type in how you feel about the day
elif mood > 5: #if mood is greater than 5
    rant = input("What made it a good day? ") # allows for you to type in how you feel about the day
elif mood == 5: # if mood is equal to 5
    rant = input("What made it just an average day? ") # allows for you to type in how you feel about the day
else:
    rant = input("What made it that way? ")# allows for you to type in how you feel about the day if you put a number outisde of 1-10
print("Thanks for telling me about your day",name) # adds name at the end of a print statement
print("Can't wait to hear more about it tomorrow!")# therapist want you to talk to them tomorow
print("Remember you are loved!")# a daily reminder.

