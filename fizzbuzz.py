for itr in range(1, 101):

    if itr % 3 == 0 and itr % 5 == 0:
        print(itr, "Fizzbuzz")
    elif itr % 3 == 0:
        print(itr, "Fizz")
    elif itr % 5 == 0:
        print(itr, "Buzz")
    else:
        print(itr)
        
        #Release branch merged into master, this is the final product.
