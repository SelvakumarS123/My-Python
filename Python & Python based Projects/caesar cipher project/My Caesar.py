alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = str(input("Type your message:\n").lower())
# shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    y = []
    for x in text:
        y.append(x)
    # print(y)
    c = ""
    # for i in range(0, len(y)):
    #     for j in alphabet:
    #         if j == text[i]:
    #             b = alphabet.index(j)
    #             y[i] = alphabet[b + shift]
    for i in range(0, len(y)):
        for j in alphabet:
            if j == text[i]:
                b = alphabet.index(j)
                s = alphabet[b:len(alphabet)]
                if len(s) > shift:
                    y[i] = alphabet[(b + shift)]
                elif len(s) <= shift:
                    s.extend(alphabet)
                    # print(s)
                    f = s[1:]
                    # print(f)
                    g = f.index(j)
                    # print(g)
                    k = s[0:g + 1]
                    # print(k)
                    t = k.index(j)
                    # print(t)
                    y[i] = s[t + shift]

    for q in y:
        c += q
    print(c)




def decrypt(text, shift):
    y = []
    for x in text:
        y.append(x)
    # print(y)
    c = ""
    for i in range(0, len(y)):
        for j in alphabet:
            if j == text[i]:
                b = alphabet.index(j)
                y[i] = alphabet[b - shift]
                # d = text.replace(text[i], alphabet[b + shift])
                # print(y)
    for q in y:
        c += q
    print(c)

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or type 'end' to end the program:\n")
    if direction == "encode":
        text = str(input("Type your message:\n").lower())
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "decode":
        text = str(input("Type your message:\n").lower())
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    elif direction == "end":
        end = True
