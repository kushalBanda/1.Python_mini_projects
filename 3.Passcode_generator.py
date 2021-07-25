import random
Passcode_or_Pin = input("Do you need a Password or a Pin : ")
if Passcode_or_Pin.lower() == 'pin':
    digits = int(input("Enter the number of digits : "))
    while digits < 4:
        digits = int(input("PIN must be at least 4 digits : "))
    Pin = str()
    for i in range(digits):
        Random_Number = random.randint(48, 57)
        Pin += (chr(Random_Number))
    print(Pin)
else:
    Easy_or_Difficult_passcode = input(
        "Do you need an Easy or a Strong passcode : ")
    if Easy_or_Difficult_passcode.lower() == 'easy':
        Easy_length = int(input("Enter the length of the easy passcode : "))
        while Easy_length < 4:
            Easy_length = int(input("Minimum length is 4 : "))
        Easy_Passcode = str()
        for i in range(Easy_length):
            Random_Number = random.randint(65, 123)
            Easy_Passcode += (chr(Random_Number))
        print(Easy_Passcode)
    else:
        Random_Number = random.randint(12, 19)
        Passcode = str()
        for i in range(Random_Number):
            Random_Number = random.randint(33, 126)
            Passcode += (chr(Random_Number))
        print(Passcode)
