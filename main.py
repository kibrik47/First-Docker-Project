#this has no meaning
print("Welcome to the multiplication table.")

def times(x):
    return [x * i for i in range(11)]

def instructions():
    print("\nPick a number between 1-10 to begin.")
    print("Type 'exit' in order to quit the program.")
    request = input("-----> ")
    return request




while True:

    user_input = instructions()

    if user_input.lower() == "exit":
        print("Exiting the program. Farewell!")
        break

    try:
        number = float(user_input)

        if 1 <= number <= 10:
            result = times(number)

            for row in range(len(result)):
                for col in range(row):
                    print(" ", end=" ")
                print(result[row])
        else:
            print("\nERROR: Invalid number. Please insert a number between 1-10 ")
    except ValueError:
        print("\nERROR: Invalid character. Please enter a number.")
