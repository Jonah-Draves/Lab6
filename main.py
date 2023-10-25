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
def main():
    user_input = 0
    while user_input != 3:
        print_menu()
        user_input = int(input('Please enter an option: '))
        if user_input == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        print()
if __name__ == '__main__':
    main()