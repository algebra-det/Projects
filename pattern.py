def first_last(digit):
    for i in range(digit):
        print("0 ", end="")
    print()

def middle(digit):
    for i in range(digit):
        if i == 0 or i == (digit-1):
            print("0 ", end="")
        else:
            print("1 ", end="")
    print()

def main():
    user_input = int(input("Enter the number : "))

    for i in range(user_input):
        if i == 0 or i == (user_input-1):
            first_last(user_input)
        else:
            middle(user_input)

if __name__ == "__main__":
    main()
