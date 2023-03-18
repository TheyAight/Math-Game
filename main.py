import random
import time
#point counter variable
points = 0

#level select that only allows select strings and will print a prompt if the input string is invalid
while True:
    level = input("what level do you want to try? \n   Easy | Normal | Hard  : ")
    accepted_strings = {'Easy', 'Normal', 'Hard'}
    if level in accepted_strings:
        tic = time.perf_counter() #starts clock 
        break
    else:
        print("Check spelling and capitalization")
# level easy that picks a random range of numbers 1-5
while level == "Easy":
    Num1 = (random.randrange(0,10))
    Num2 = (random.randrange(0,10))
    sum = Num1 + Num2 #sets the correct answer
#asks user for input then will comparec it against the correct answer
    ans = int(input("{} + {} = ".format(Num1,Num2)))
    if ans == sum:
        print("Correct!")
        points = points + 1
    else:
        print("Incorrect")
        toc = time.perf_counter()
        tim = toc - tic #used to end the clock so it can be printed to screen
        print("You scored {} in {} seconds.\nProgram will close soon, please wait.".format(points, round(tim,2)))
        time.sleep(5) #stops the program for 5 seconds before quit
        break
   
while level == "Normal":
    Num1 = (random.randrange(0,11))
    Num2 = (random.randrange(0,11))

    Alg = (random.randrange(0,10))

    if Alg >= 5:
        sum = Num1 * Num2
        ans = int(input("{} * {} = ".format(Num1,Num2)))
        if sum == ans:
            print("Correct!")
            points = points + 2
            continue
        else:
            print("Incorrect!")
            toc = time.perf_counter()
            tim = toc - tic
            print("You scored {} in {} seconds.\nProgram will close soon, please wait.".format(points, round(tim,2)))
            time.sleep(5)
            break
    elif Alg <= 4:
        sum = Num1 + Num2
        ans = int(input("{} + {} = ".format(Num1,Num2)))
        if sum == ans:
            print("Correct!")
            points = points + 1
            continue
        else:
            print("Incorrect!")
            toc = time.perf_counter()
            tim = toc - tic
            print("You scored {} in {} seconds.\nProgram will close soon, please wait.".format(points, round(tim,2)))
            time.sleep(5)
            break
while level == "Hard":
    Num1 = (random.randrange(0,16))
    Num2 = (random.randrange(0,16))

    Alg = (random.randrange(1,4))

    if Alg == 1:
        sum = Num1 * Num2
        ans = int(input("{} * {} = ".format(Num1,Num2)))
        if sum == ans:
            print("Correct!")
            points = points + 2
            continue
        else:
            print("Incorrect!")
            toc = time.perf_counter()
            tim = toc - tic
            print("You scored {} in {} seconds.\nProgram will close soon, please wait.".format(points, round(tim,2)))
            time.sleep(5)
            break
    elif Alg == 2:
        sum = Num1 + Num2
        ans = int(input("{} + {} = ".format(Num1,Num2)))
        if sum == ans:
            print("Correct!")
            points = points + 1
            continue
        else:
            print("Incorrect!")
            toc = time.perf_counter()
            tim = toc - tic
            print("You scored {} in {} seconds.\nProgram will close soon, please wait.".format(points, round(tim,2)))
            time.sleep(5)
            break
    else:
        sum = Num1 / Num2
        sum2 = round(sum, 2)
        ans = float(input("{} / {} = ".format(Num1,Num2)))
        if sum2 == ans:
            print("Correct!")
            points = points + 3
            continue
        else:
            print("Incorrect!")
            toc = time.perf_counter()
            tim = toc - tic
            print("You scored {} in {} seconds.\nProgram will close soon, please wait.".format(points, round(tim,2)))
            time.sleep(5)
            break

