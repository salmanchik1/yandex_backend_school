with open('input.txt', 'r') as source:
    string = source.read()
a, b = map(int, string.split(' '))
with open('output.txt', 'w') as destination:
    destination.write(str(a + b))
