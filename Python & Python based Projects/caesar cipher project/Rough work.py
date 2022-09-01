from typing import List, Any, Union

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = str(input("Type your message:\n").lower())
# n = alphabet.index("n")
# print(alphabet[0:n])
b = alphabet.index("n")
s = alphabet[b:len(alphabet)]
s.extend(alphabet)
print(s)
f = s[1:]
# print(f)
g = f.index("n")
# print(g)
k = s[0:g]
# print(k)
t = k.index("n")
# print(t)