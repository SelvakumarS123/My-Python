
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_letter = alphabet[position + shift_amount]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"the encrypted text is, {cipher_text}")


# the wonderful thing about the index function is it's gonna give you the first index that it finds.
# If you're looking for the index of 'a' it"s gonna give you '0' and stop looking.
# Hence, it is good idea to just duplicate the list(alphabet) once again.


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_letter = alphabet[position - shift_amount]
            plain_text += new_letter
        else:
            plain_text += letter
    print(f"the decrypted text is, {plain_text}")


end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or type 'end' to end the program:\n")
    if direction == "encode":
        text = str(input("Type your message:\n").lower())
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        text = str(input("Type your message:\n").lower())
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        decrypt(cipher_text=text, shift_amount=shift)
    elif direction == "end":
        end = True

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = str(input("Type your message:\n").lower())
# shift = int(input("Type the shift number:\n"))
