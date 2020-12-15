name = input('Whats your name?')

decent_moods = ["eh","average","so so"]
good_moods = ["good","great","amazing","awesome"]
bad_moods = ["bad","terrible","not good"]

mood = input('How was your day {}?'.format(name))

if mood in good_moods:
    print("That's awesome!")
    goodmoodtalk = input("What made it a good day?")
    print("That sounds great!")
    keep_talking = input("Would you like to keep talking?")
    while keep_talking.lower() == "yes":
        more_talk = input("Okay! Tell me more. Im listening")
        keep_talking = input("Would you like to keep talking?")
    else:
        print("Thanks for telling me about your day {}. Can't wait to hear about it tomorrow!".format(name))
elif mood in decent_moods:
    print("I can tell its going to get better!")
    decentmoodtalk = input("What could have made the day better?")
    keep_talking = input("Would you like to keep talking?")
    while keep_talking.lower() == "yes":
        more_talk = input("Okay! Tell me more. Im listening")
        keep_talking = input("Would you like to keep talking?")
    else:
        print("Thanks for telling me about your day {}. Can't wait to hear about it tomorrow!".format(name))
elif mood in bad_moods:
    print("Oh no. Hopefully tomorrow will be better!")
    badmoodtalk = input("Do you want to talk about it?")
    keep_talking = input("Would you like to keep talking?")
    while keep_talking.lower() == "yes":
        more_talk = input("Okay! Tell me more. Im listening")
        keep_talking = input("Would you like to keep talking?")
    else:
        print("Thanks for telling me about your day {}. Can't wait to hear about it tomorrow!".format(name))
else:
    mood = input("Was it overall good, bad, or decent")
    keep_talking = input("Would you like to keep talking?")
    while keep_talking.lower() == "yes":
        more_talk = input("Okay! Tell me more. Im listening")
        keep_talking = input("Would you like to keep talking?")
    else:
        print("Thanks for telling me about your day {}. Can't wait to hear about it tomorrow!".format(name))
