alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = str(input("Type your message:\n").lower())
shift = int(input("Type the shift number:\n"))
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



for q in y:
    c += q
print(c)



