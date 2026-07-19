"""password char and digit for safe"""

character = input()
digit = input()

if character == "H" and digit == "4567" :
    print("safe unlocked")
elif character == "H" and digit != "4567" :
    print("safe locked - change digit")
elif character != "H" and digit == "4567" :
    print("safe locked - change char")
else :
    print("safe locked")
