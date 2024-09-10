def fizz_buzz():
    num = int(input("How many numbers do hyou want to fizzBuzz? -> "))
    count = 1
    while count <= num:
        if count % 3 == 0 and count % 5 == 0:
            print("fizz buzz")
        elif count % 5 == 0:
            print("buzz")
        elif count % 3 == 0:
            print("fizz")
        else:
            print(count)
        count = count + 1

if __name__ == '__main__':
    print("Hello World from bonus_functions.py")

