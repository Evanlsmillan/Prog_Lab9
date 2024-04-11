# This is Nathans code

def encode(password):
    empty = ''
    for i in password:
        y = 3
        if int(i) > 6:
            x = (int(i) + 3) % 10
        else:
            x = int(i) + y
        empty = empty + str(x)
    return empty
print(encode('00009962'))

if __name__ == '__main__':
    menu = """Menu
-------------
1. Encode
2. Decode
3. Quit
"""
    while True:
        print(menu)
        choice = input('Please enter an option: ')
        if choice == '1':
            password = input('Please enter your password to encode: ')
            print(encode(password))
            print("Your password has been encoded and stored!")

        if choice == '2':
            decode = input('Please enter an option: ')
            
        if choice == '3':
            exit()