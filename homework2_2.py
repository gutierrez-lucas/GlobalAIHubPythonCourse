"""
SECOND HOMEWORK

2) Ask de user to input a single digit integer to a variable 'n'.
Then, print out all of the even numbers from 0 to n (including n)

"""

conditionVerified = False

while conditionVerified == False:
    n = int(input("Please insert a single digit value: ")) #cast the char inputo to int so it can be used as a number
    print("You selected: ", n)
    if n > 9:
        print("ERROR: the value must be a single digit one...")
    else:
        conditionVerified = True

list = [i for i in range(0, n + 1) if i % 2 == 0]
print("List: ", list)