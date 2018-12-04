import re

print("My Calculator")
print("Type 'quit' to exit\n ")

previous = 0
run = True
def MyCalci():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter a Equation: ")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Thanks")
        run = False
    else:

        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous==0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)

while run:
    MyCalci()

