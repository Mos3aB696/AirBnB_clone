#!/usr/bin/python3
"""class HBNBCommand"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnp) '

    def do_quit(self, args):
        """Quit or exit the program"""
        return True
    
    def do_EOF(self, args):
        """Exit of the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
