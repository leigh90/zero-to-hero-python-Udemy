# when you run your file anything at indentation level zero gets run

# __name__ # this is an inbuilt python variable it gets assigned a string depending on how you run the file
# if you run the script directly 'python3.6 one.py'  python equates that variable __name__ to __main__ to check if they are equal to each other

# when a file is run directly python equates __name__ to __main__ as in the case below where if you run "python3.6 one.py" the first block of the if statement is executed
# otherwise __name__ does not equal __main__
# thats why when "two.py is run instead the second block of the if statement is run instead. because the functions in one.py are run by virtue of having been imported and called inside two.py and not directly run"

def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")
if __name__ == '__main__':
    print('ONE.PY is being run directly!')
else:
    print("ONE.PY has been imported")

def function2():
    pass

def function3():
    pass

# TYPICAL USAGE
if __name__ == "__main__":
    function2()
    function3()
    # here the functions you have created above are called here


