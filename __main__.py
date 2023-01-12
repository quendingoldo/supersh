from supersh_control import globs, supersh_valid

PROMPT = '$$=> '
HELPFILE = 'help.txt'

var = {}

while True:
    # Load input and check its validity.
    cmd = input(PROMPT).strip()
    valid = supersh_valid(cmd, var)
    if not valid:
        print(valid)
        continue

    # If input is valid, evaluate commands or expressions
    # HERE 
    if ...:
        pass




    else:
        print(eval(cmd, globs | var))
