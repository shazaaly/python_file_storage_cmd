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


if __name__ == "__main__":
    MyCmd().cmdloop()
