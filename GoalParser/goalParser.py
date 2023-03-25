def interpret(command: str) -> str:
        commandString = ""
        parser_dict = {
            "G": "G",
            "()": "o",
            "(al)": "al"
        }
        previous = ""
        for c in command:
            if c == "(":
                previous = c
            elif c == "a" and previous == "(":
                previous += c
            elif c == "l" and previous == "(a":
                previous += c
            elif c == ")":
                commandString += parser_dict[previous + c]
                previous = ""
            else:
                 commandString += parser_dict[c]

        return commandString

command = "G()()()()(al)"
results = interpret(command)
print(results)