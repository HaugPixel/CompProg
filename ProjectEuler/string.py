linje = input().lower()
key2d = []

for char in linje:
    if char not in key2d and char != " ":
        key2d.append(char)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for char in alphabet:
    if len(key2d) == 25:
        break
    if char not in key2d:
        key2d.append(char)

n = 5
key = [key2d[i:i+n] for i in range(0, len(key2d), n)]
# Dont change

message = input().replace(" ", "")
doubles = []

for i in range(0, len(message)-1, 2):
    doubles.append((message[i], message[i+1]))

if len(message) % 2:
    doubles.append(message[len(message)-1])




