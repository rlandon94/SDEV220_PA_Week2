guess_me = 5

number = (10)

for number in range(1,10):

    if number < guess_me:
        print("too low")
        number += 1

    elif number == guess_me:
        print("found it!")
        break

    else:
        print("oops")
        break
