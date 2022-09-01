from caesar_arts import logo
from caesar_arts import alphabet
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_letter = alphabet[position + shift_amount]
            end_text += new_letter
        else:
            end_text += letter
            # here the 'letter' denotes any other characters like ' '(space) or ! or @ etc. that are not in the alphabet
    print(f"the {cipher_direction}d text is {end_text}")


end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = str(input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    again = str(input("Type 'yes' if you wanna go again. otherwise type 'no'.\n"))
    if again == 'no':
        end = True
        print("Good bye!")
