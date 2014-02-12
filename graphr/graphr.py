import sympy
from sympy.parsing.sympy_parser import parse_expr
import inspect

x = sympy.symbols("x")

class Graphr:
    def __init__(self):
        self.running = False
        self.settings = {
            "prompt"        : "graphr => ",
        }
        self.operations = {
            "diff"          : sympy.diff,
            "integrate"     : sympy.integrate,
            "exit"          : self.exit,
        }

    def run(self):
        self.running = True
        while self.running:
            #program logic contained in main() to isolate it from gui logic which will be implemented later
            self.main()

    def main(self):
        """Gets and executes user input"""
        input_list = self.get_input()
        command = input_list.pop(0)
        if command in self.operations:
            operation = self.operations[command]
            try:
                ans = operation(*input_list)
                print ans
            except TypeError:
                print "Incorrect arguments passed for '%s' operation." % command
                print inspect.getargspec(operation)
        else:
            print "Command '%s' not recognised." % command

    def get_input(self):
        """Returns list of input terms seperated by a space."""
        input_string = raw_input(self.settings["prompt"]).lower()
        input_list = input_string.split(" ")
        return input_list

    def exit(self):
        self.running = False

def main():
    graphr = Graphr()
    graphr.run()

if __name__ == "__main__":
    main()