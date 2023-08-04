import cmd


class MyCmd(cmd.Cmd):
    prompt = "(hbnb) "

    def do_hello(self, arg):
        print("Hello this is your cmd : ")

    def do_quit(self, arg):
        print("Goodbuy..")
        return True

    def emptyline(self):
        pass

    def default(self, line):
        print(f"this is an unknown command: {line}")


if __name__ == "__main__":
    MyCmd().cmdloop()
