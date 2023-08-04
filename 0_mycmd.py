import cmd
from typing import Any


class MyCmd(cmd.Cmd):
    prompt = "(hbnb) "

    def do_hello(self, arg):
        print("this is your cmd : ")

    def do_quit(self, arg):
        print("Goodbuy..")
        return True

    def emptyline(self):
        pass

    def default(self, line):
        print(f"this is an unknown command: {line}")

    def completedefault(self, text, line, begidx, endidx):
        commands = ["get", "mycommand"]
        completions = [cmd for cmd in commands if cmd.startswith(text)]
        return completions

    def precmd(self, line: str):
        print("Validate command...")
        return line


if __name__ == "__main__":
    MyCmd().cmdloop()
