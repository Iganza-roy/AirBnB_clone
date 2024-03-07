#!/usr/bin/python3
"""Entry point of the command interprator"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines a class to the cmd interprator"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing if empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
