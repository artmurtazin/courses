
a = float(input())
b = float(input())
o = str(input())

r = 1

if o == "/":
    if b == 0:
        print('Деление на 0!')
    else:
        r = a / b
        print(r)

if o == "+":
    r = a + b
    print(r)

if o == "-":
    r = a - b
    print(r)

if o == "*":
    r = a * b
    print(r)

if o == "mod":
    r = a % b
    print(r)   

if o == "pow":
    r = a ** b
    print(r)

if o == "div":
    r = a // b
    print(r)