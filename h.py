def main():
    user_input = input("Enter the String : ").lower()

    dict = { "key" : 0 }

    completed_char = []

    for i in range(len(user_input)-1):
        count = 0
        if i not in completed_char:
            for j in range(len(user_input)):
                if user_input[i] == user_input[j]:
                    count += 1

            dict[user_input[i]] = count
            completed_char.append(user_input[i])

    the_key = max(dict, key=dict.get)
    the_value = dict.get(the_key)

    print(the_key, " = ", the_value)

if __name__ == "__main__":
    main()
