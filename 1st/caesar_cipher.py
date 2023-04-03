
# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o',
#              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
# text = input('Type your message:\n').lower()
# shift = int(input("Type shift number:\n"))
# def encrypt(plain_text,shift_amount):
#     ciphers_text = ""
#     for letter in plain_text:
#         position = alphabets.index(letter)
#         new_position = position+shift_amount
#         new_letter = alphabets[new_position]
#         ciphers_text = ciphers_text+new_letter
#         #print(position)
#     print(f'The encoded text is {ciphers_text}')
#
# def decrypt(ciphers_text,shift_amount):
#     plain_text = ''
#     for letter in ciphers_text:
#         position = alphabets.index(letter)
#         new_position = shift_amount-position
#         new_letters = alphabets[new_position]
#         plain_text += new_letters
#         print(position, new_position)
#     print(f' your decode text is {plain_text}')
#
# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(ciphers_text=text, shift_amount=shift)
# else:
#     print('Please type eighter "encode" and "decode"')

############################################################

# new function ceasar() function which is combination of encrypt and decrypt function,
# passing over the text, shift and direction
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True  # FLAG for using while loop
while should_continue:  # if user want to continue typing code and decode

    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    text = input('Type your message:\n').lower()
    shift = int(input("Type shift number:\n"))
    shift = shift % 26     # 26 alphabets for having greater shift values
#                            and to save code from breaking down

    def caesar(start_text, shift_amount, cipher_direction):     # to diff from above values
        if cipher_direction == 'decode':
            shift_amount *= -1
        for letter in start_text:
            if letter in alphabets:  # if we use space,symbols out of alphabet range
                position = alphabets.index(letter)
                new_position = position-shift_amount
                end_text = alphabets[new_position]
                print(f'{cipher_direction} is {end_text}')
            else:
                end_text += letter

    caesar(shift_amount=shift, start_text=text, cipher_direction=direction)
    result = input('Type "yes" if you want to continue. Otherwise type "no".\n')
    if result == "no":
        should_continue = False
        print('Goodbye')