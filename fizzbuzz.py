for itr in range(1, 101):

    if itr % 3 == 0 and itr % 5 == 0:
        print(itr, "Fizzbuzz")
    elif itr % 3 == 0:
        print(itr, "Fizz")
    elif itr % 5 == 0:
        print(itr, "Buzz")
    else:
        print(itr)
#This is the last branch - the release branch gets released to master.