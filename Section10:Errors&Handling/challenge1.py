# Problem 1: Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a', 'b','c']:
        print(i**2)
except:
    print("You cannot square non numbers")

# Problem 2: Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
def divide(x,y):
    try:
       z = x/y
       print(z)
    except ZeroDivisionError:
        print("You cannot divide a number by Zero")
    finally:
        print("All done")

divide(3,7)
divide(5,0)

# Problem 3: Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def num_square():
    while True:
        try:
            num = int(input("Please provide a number "))
            num = num ** 2
            print(num)
        except:
            print("That was not a number")
        else:
            break

num_square()

            
   

