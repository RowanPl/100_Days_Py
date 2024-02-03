alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
ceasar = True


# def encrypt(text, shift):
#     encrypted_text = ""
#     for char in text:
#         char_index = alphabet.index(char)
#         char_index = (char_index + shift) % 26
#         encrypted_text += alphabet[char_index]
#
#     print(f" the decoded text is : {encrypted_text}")
#
#
# def decrypt(p_text, n_shift):
#     decoded_text = ""
#     for char in p_text:
#         char_index = alphabet.index(char)
#         char_index = (char_index - n_shift) % 26
#         decoded_text += alphabet[char_index]
#
#     print(f" the decoded text is : {decoded_text}")

def ceasar_cipher(text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)

            new_char_index = char_index + shift_amount
            end_text += alphabet[new_char_index]
        else:
            end_text += char
    print(f"the {cipher_direction}d text is : {end_text}")


while ceasar:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar_cipher(text, shift, direction)
    choice = input("Would you like to encrypt/decrypt again?")
    if choice == "n":
        print("Thanks for using this application")
        ceasar = False
