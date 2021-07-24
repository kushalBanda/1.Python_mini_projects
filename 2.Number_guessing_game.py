import random
Start_point = input("Enter the start point : ")
while Start_point.isnumeric() != True:
    Start_point = input("Please , enter a whole number : ")
End_point = input("Enter the end point : ")
while End_point.isnumeric() != True:
    End_point = input("Please , enter a whole number : ")
random_number = random.randint(int(Start_point), int(End_point) + 1)

turns = int(1)
flag = int(-1)
while 1 == 1:
    guess = int(
        input("Guess a number in the range (inclusive of Start_point and End_Point) : "))
    if flag == 0:
        break
    if guess >= int(Start_point) and guess <= int(End_point):
        if guess != random_number:
            print("Wrong Guess")
            turns += 1
        else:
            flag += 1
            break
    else:
        print("Enter a number between ", str(
            Start_point), "and", str(End_point))
if turns == 1:
    print("Number of turns taken are to guess the " +
          str(random_number), "is" + str(turns))
else:
    print("Number of turns taken are to guess the " +
          str(random_number), "are " + str(turns))
