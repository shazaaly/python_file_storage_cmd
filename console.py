#!/usr/bin/python3

import cmd
import sys
from typing import Any


class MyCmd(cmd.Cmd):

    prompt = "(hbnb) "

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

    def do_quit(self, arg):
        """Exit command Interpretter"""
        return

    def do_EOF(self, line):
        """Exit command Interpretter"""
        return True

    def postcmd(self, stop: bool, line: str) -> bool:

        if not stop:
            if line.strip() == "quit":
                print("$")
                return True
        return stop

    # def do_help(self, arg):
        """customize help command"""
        print("(hbnb)")
        print()
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF help quit")
        # print()
        print("(hbnb)")


if __name__ == "__main__":
    mycmd = MyCmd()
    # chck if input is coming from a pipe:
    if not sys.stdin.isatty():
        lines = sys.stdin.read().splitlines()
        for line in lines:
            print("(hbnb)")
            mycmd.onecmd(line)
        print("(hbnb)")
        print("$")
        sys.exit()

        # If command-line arguments:
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            mycmd.onecmd(arg)

    else:
        mycmd.cmdloop()
