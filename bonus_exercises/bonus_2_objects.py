while True:

    password = input("Create a strong password: ")

    result = {}

    if len(password) > 8:
        result['password'] = True
    else:
        result['password'] = False

    has_number = False

    for i in password:

        if i.isdigit():
            has_number = True

    result['number'] = True

    has_uppercase = has_number

    for i in password:

        if i.isupper():
            has_uppercase = True

    result['uppercase'] = has_uppercase

    if all(result.values()):
        print("Strong password")
        print("Write it down")
        break
    else:
        print(len(result))
        print(result[1])
        print("Weak password")


