def encoder(pw):  # encodes password by adding 3 to each digit
    for i in len(pw):
        pw[i] = str(int(pw[i]) + 3)
    return pw


def decoder(pw):
    for i in len(pw):
        pw[i] = str(int(pw[i]) - 3)
    return pw


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu = "Menu\n----------\n1. Encode\n2. Decode\n3. Quit\n\n"  # menu string variable
    print(menu)
    choice = 4
    password = ""
    while choice != 3:  # runs until choice == 3 (exit option chosen)
        choice = int(input('Please enter an option: '))
        if choice == 1:  # encodes password
            password = input('Please enter your password to encode: ')
            password = encoder(password)
            print('Your password has been encoded and stored!')
        elif choice == 2:  # decodes password
            decoded = decoder(password)
            print(f'The encoded password is {password}, and the original password is {decoded}.')