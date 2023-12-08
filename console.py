#!/usr/bin/python3
"""class HBNBCommand"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit or exit the program"""
        return True

    def do_create(self, args):
        """Create New Instance Of BaseModel"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = args.split()
        if len(args) > 0 and args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            for key, val in models.storage.all().items():
                if len(args) == 0 or args[0] == key.split(".")[0]:
                    print(str(val))

    def do_update(self, args):
        """Updates an instance based on the class name and id by
        adding or updating attribute """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in models.storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if args[2] not in ["id", "created_at", "updated_at"]:
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.all()[key].save()

    def do_EOF(self, args):
        """Exit of the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
