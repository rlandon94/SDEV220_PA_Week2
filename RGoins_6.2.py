guess_me = 7

number = 1

while  number < guess_me:
    print("too low")
    number += 1

while number > guess_me:
    print("oops")
    break

while number == guess_me:
    print("found it!")
    break