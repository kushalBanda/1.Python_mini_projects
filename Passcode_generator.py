import random
Easy_or_Difficult_passcode = input(
    "Do you need an easy or a difficult passcode : ")
if Easy_or_Difficult_passcode.lower() == 'easy':
    Easy_length = int(input("Enter the length of the easy passcode : "))
    Easy_Passcode = str()
    for i in range(Easy_length):
        Random_Number = random.randint(65, 123)
        Easy_Passcode += (chr(Random_Number))
    print(Easy_Passcode)
else:
    print(Easy_or_Difficult_passcode)
    Length = int(input("Enter the length of the difficult passcode : "))
    Passcode = str()
    for i in range(Length):
        Random_Number = random.randint(33, 123)
        Passcode += (chr(Random_Number))
    print(Passcode)
