from supersh_control import welcome, globs, supersh_valid

PROMPT = '$$=> '
HELPFILE = 'help.txt'
var = {}  #here are stored variables

# show welcome info
welcome()


while True:
    # Load input and check its validity.
    cmd = input(PROMPT).strip()
    valid = supersh_valid(cmd, var)
    if not valid:
        print(valid)
        continue

    # If input is valid, evaluate commands or expressions
    # ↓↓↓ HERE WRITE YOUR CODE ↓↓↓
    elif ...:
        pass


    else:
        # If the input is only an expression, print value
        print(eval(cmd, globs | var))


