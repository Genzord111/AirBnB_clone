#!/usr/bin/python3
"""(module) This module contains the HBNBCommand object"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This object inherits from the cmd class
    to create a custom command interpreter for
    managing the AirBnB clone database"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        raise SystemExit

    def emptyline(self):
        """Prevents termination of program by blankline
        + ENTER"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
