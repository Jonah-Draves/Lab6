def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    return None
def encode(password):
    encoded = ''
    for char in password:
        if int(char) + 3 <= 9:
            encoded += str(int(char) + 3)
        else:
            encoded += str(int(char) - 7)
    return encoded
def decode(password):
    passwordlist = []
    decoded = ''
    password.split()
    for i in range(0, len(password)):
        passwordlist.append((int(password[i]) + 7) % 10)
        decoded += str(passwordlist[i])
    print(f'The encoded password is {password}, and the original password is {decoded}.')
    return decoded
def main():
    user_input = 0
    while user_input != 3:
        print_menu()
        user_input = int(input('Please enter an option: '))
        if user_input == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif user_input == 2:
            decode(encoded_password)
        print()
if __name__ == '__main__':
    main()