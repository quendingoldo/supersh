import os

globs = {'__name__': '', '__doc__': '', '__package__': {}, '__loader__': {}, 
        '__spec__': {}, '__annotations__': {}, '__builtins__': {}}

error_type = {
        SyntaxError: 'NotSupershSyntaxError',
        NameError: 'NoVariableWithThatNameError',
        ZeroDivisionError: 'CantDevideByZeroError',
        TypeError: 'MessedTypesError'
    }


class SupershError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return False


def supersh_valid(cmd: str, 
                  var: dict[str, int | float | str]) -> bool | SupershError:
    if cmd in {'#exit', '#help', '#save'}:
        return True

    elif cmd.startswith('#load'):
        if cmd == '#load':
            file = 'vars.txt'
        else:
            file = cmd[6:]
        if file not in os.listdir():
            return SupershError('FileDoesNotExistError')
        return True
    
    elif cmd.startswith('#save'):
        file = cmd[6:]
        if '.' not in file or any([x in file for x in r"""#/|\$%!`<>*&?="':@{}"""]):
            return SupershError('InvalidFileNameError')

    elif cmd.startswith('$') or cmd.startswith('#var '):
        if cmd[0] == '#':
            cmd = cmd[5:]
        elif cmd[0] == '$':
            cmd = cmd[1:]
        if ' = ' not in cmd:
            return SupershError(error_type[SyntaxError])
        name, value = cmd.split(' = ')
        charset = set(range(65, 91)).union(set(range(97, 123))).union({95}).union(range(48, 58))
        if any([ord(char) not in charset for char in name]) or name[0].isdigit():
            return SupershError('InvalidVariableNameError')
        cmd = value
    try:
        eval(cmd, globs | var)
    except (SyntaxError, NameError, ZeroDivisionError, TypeError) as exc:
        return SupershError(error_type[type(exc)])
    return True
