num = 100

for itr in range(1, num + 1):

    if itr % 3 == 0 and itr % 5 == 0:
        print(itr, "Fizzbuzz")
    elif itr % 3 == 0:
        print(itr, "Fizz")
    elif itr % 5 == 0:
        print(itr, "Buzz")
    else:
        print(itr)
# This is a comment to show how branches work


