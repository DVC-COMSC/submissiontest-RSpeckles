inputs = []
while True:
    i = input("Enter some text: ")
    if i != "stop" and i != "STOP":
        inputs.append(i)
    else:
        break

longest = inputs[0]
shortest = inputs[0]

for j in range(0, len(inputs)-1):
    if len(inputs[j+1]) < len(shortest):
        shortest = inputs[j+1]
    elif len(inputs[j+1]) >= len(longest):
        longest = inputs[j+1]

print(shortest)
print(longest)