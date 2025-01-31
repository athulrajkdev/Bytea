from bytea.lexer import Lexer
from bytea.parser import Parser
from bytea.interpreter import Interpreter
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: bytea <file.bta>")
        return

    filename = sys.argv[1]
    try:
        with open(filename, "r") as file:
            code = file.read()
        lexer = Lexer(code)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        interpreter = Interpreter(ast)
        interpreter.run()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()