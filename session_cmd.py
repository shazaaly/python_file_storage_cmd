#!/usr/bin/python3

import cmd


class SimpleShell(cmd.Cmd):
	prompt = ("shell>> ")
	intro = "Welcome to the Simple Shell! Type help or ? to list commands.\n"

	def do_greet(self, line):
		"""Greet someone."""
		print(f"Hello, {line}!")

	def complete_greet(self, text, line, begidx, endidx):
		friends = ['Alice', 'Bob', 'Charlie']
		if not text:
			completions = friends[:]
		else:
			completions = [f for f in friends if f.startswith(text)]
		return completions





if __name__ == '__main__':
	SimpleShell().cmdloop()
