while True:
    print("Please choose an option:\n1:vote\n2:return the next movie\n3:quit")
    option = input()
    if option == "1":
        print("What movie do you want to vote for?")
        movie = input()
        # some rest call
        print("You have successfully voted for" + movie)
    elif option == "2":
        # some rest call
        result = False
        if result == False:
            print("there are no movies in the waiting list :(")
        else:
            print("The next movie we should watch is " + result)
    elif option == "3":
        # some rest call
        break
    else:
        print("invalid input")
