def main():
    #problem1()
    #problem2()
    #problem3()
    problem4()

#Print -20 to and including 50. Use any loop you want.
def problem1():
    for i in range(-20, 50):
        print(i)

#Create a loop that prints even numbers from 0 to and including 20.
def problem2():
    for i in range(0, 22, 2):
        print(i)

#Prompt the user for 3 numbers. Then print the  3 numbers along with their average
# after the 3rd number is entered. Refer to example below replacing NUMBER1,
# NUMBER2, NUMBER3, and THEAVERAGE with the actual values.
def problem3():
    varNum1 = int(input("Enter number"))
    varNum2 = int(input("Enter number"))
    varNum3 = int(input("Enter number"))
    varAverage = (varNum1+varNum2+varNum3)/3
    print("The average of " +  str(varNum1) + " "+ str(varNum2) + " "+ str(varNum3),"is" + " " + " "+ str(varAverage))

#Password Checker - Ask the user to enter a password. Ask them to confirm the password.
# If it's not equal, keep asking until it's correct or they enter 'Q' to quit.
def problem4():
    varInput1 = input("Enter password")
    varInput2 = input("Confirm password")
    if varInput1 != varInput2:
        print 





























if __name__ == '__main__':
    main()