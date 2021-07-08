nums = [23, 53, 34, 12, 84, 24, 98]

while True:
    answer = input("Guess a number or type q to quit")
    if answer == 'q':
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in nums:
        print("Your guessed are right!")
    else:
        print("Your guessed are wrong!")
