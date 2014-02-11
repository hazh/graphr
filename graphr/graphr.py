import sympy
from sympy.parsing.sympy_parser import parse_expr

x = sympy.symbols("x")

class Graphr:
    def __init__(self):
        self.running = False
        self.settings = {
            "prompt"        : "graphr => ",
        }
        self.functions = {
            "diff"          : sympy.diff,
            "integrate"     : sympy.integrate,
        }

    def run(self):
        self.running = True
        while self.running:
            input_string = raw_input(self.settings["prompt"]).lower()
            input_list = input_string.split(" ", 1)
            command = input_list[0]
            if command == "exit":
                self.exit()
            elif command in self.functions:
                expression = parse_expr(input_list[1])
                ans = self.functions[command](expression, x)
                print ans
            else:
                print "Command '%s' not recognised." % command
                continue

    def exit(self):
        self.running = False
            

def main():
    graphr = Graphr()
    graphr.run()

if __name__ == "__main__":
    main()