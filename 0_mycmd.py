import cmd


class MyCmd(cmd.Cmd):
    prompt = "(hbnb) "

    def do_hello(self, arg):
        print("Hello this is your cmd : ")


if __name__ == "__main__":
    MyCmd().cmdloop()
