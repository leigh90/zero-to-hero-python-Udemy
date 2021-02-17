# ERROR HANDLING KEYWORDS
# TRY - Block of code attempted which may or may not lead to an erro
# EXCEPT - Block of code which will execute in case there is an error in the try block
# FINALLY - A final block of code to be executed, regardless of an error
# The try except block allows the code to run even after an error instead of stoopping the whole thing

# try:
#     # attempt this code may have an error
#     result = 10 + 10
#     # the above line of code will execute properly and trigger the else block
#     # result2 = 10 + '10'
#     # the above line will not execute properly and thus trigger the except block
# except:
#     print("You are not adding correctly")
# else:
#     print("Add went well!")
#     print(result)

# EXAMPLE2
# try:
#     # f= open('testfile','w') #open a file in write mode
#     # lets introduce an error lets open testfile in read only then try to write to it. this will invoke the OSError that prevents files in read-only mde from being written to 
#     f = open('testfile','r')
#     f.write("Write a test line")
# except TypeError:
#     print("There was a type error")
# except OSError:
#     print("Hey you have an OS Error")
# finally:
#     print("I always run")
    # will always run regardless of any errors

    # note that for the except plock you can either mention the specific error or you can leave it to handle all errors.
    # for example except TypeError or just except

# EXAMPLE 2

# def ask_for_int():

#     try:
#         result = int(input("Please provide a number: "))
#         print(result)
#     except:
#         print("Whoops that is not a number")
#     finally: 
#         print("End of try/except/finally")

# ask_for_int()

# adding a while loop
def ask_for_int():
    waiting = True
    while waiting:
        try:
            result = int(input("Please provide a number: "))
            print(result)
        except:
            print("Whoops that is not a number")
            continue
        else:
            print("Thank You")
            waiting = False # You can use this if you dont want to use the break statement
            # break #will break out of the loop if a number is provided

        # finally: 
        #     print("End of try/except/finally")
        #     print("I will always run at the end ")


ask_for_int()

    
    