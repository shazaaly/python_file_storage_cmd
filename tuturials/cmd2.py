#!/usr/bin/python3

import cmd


class MyCmd(cmd.Cmd):
    prompt = ">> "

    def do_sum(self, args):
        nums = [int(num) for num in args]
        print(f"Sum: {sum(nums)}")


if __name__ == "__main__":
    MyCmd().cmdloop()
