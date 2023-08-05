#!/usr/bin/python3

import cmd
import sys
from typing import Any


class MyCmd(cmd.Cmd):
    prompt = "(hbnb) "

    def do_hello(self, arg):
        print("Hello, this is your cmd")

    def do_greet(self, arg):
        print("Greetings... ")

    def do_quit(self, arg):
        return True

    def emptyline(self):
        pass

    def default(self, line):
        print(f"this is an unknown command: {line}")

    def completedefault(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]

        completions = [f for f in self.FRIENDS if f.startswith(text)]
        return completions

    # def precmd(self, line: str):
        print("Validate command...")
        return line

    def do_exit(self, arg):
        print("Exiting...")
        return

    def do_EOF(self, line):
        return True

    def postcmd(self, stop: bool, line: str) -> bool:

        if not stop:
            if line.strip() == "quit":
                print("$")
                return True
        return stop

    def preloop(self) -> None:
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF help quit")
        print("		")
        print("		")


if __name__ == "__main__":
    mycmd = MyCmd()
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            mycmd.onecmd(arg)

    else:
        mycmd.cmdloop()
