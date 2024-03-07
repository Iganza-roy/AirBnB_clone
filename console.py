#!/usr/bin/python3
"""Entry point of the command interprator"""
import cmd
import json
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines a class to the cmd interprator"""

    prompt = "(hbnb) "

    __classes = {
            "BaseModel" : BaseModel
            }

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

    def parse(self, arg):
        """Parses args and matches commands"""
        args = arg.split()
        if not args:
            return None
        cls_name = args[0]
        cls = self.__classes.get(cls_name)
        if not cls:
            print("** class doesn't exist **")
            return None
        return cls

    def do_create(self, arg):
        """Creates a new instance of provided class"""
        if not arg:
            print("** class name missing **")
            return

        cls = self.parse(arg)
        if cls:
            new_inst = cls()
            new_inst.save()
            storage.new(new_inst)
            storage.save()
            print(new_inst.id)

    def do_show(self, arg):
        """Prints string rep of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        cls = self.parse(args[0])
        if not cls:
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        inst = storage.all()
        key = "{}.{}".format(args[0], args[1])

        if key not in inst:
            print("** no instance found **")
            return
        print(inst[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]

        if cls_name not in self.__classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return

        inst_id  = args[1]
        insts = storage.all()
        key = "{}.{}".format(cls_name, inst_id)


        if key not in insts:
            print("** no instance found **")
            return

        del insts[key]
        storage.save()


    def do_all(self, arg):
        """Prints all string reps of instances"""
        args = arg.split()
        inst_list = []
        insts = storage.all()

        if args and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return

        if args:
            cls_name = args[0]
            for key, inst in insts.items():
                if key.startswith(cls_name + "."):
                    inst_list.append(str(inst))
        else:
            for inst in insts.values():
                inst_list.append(str(inst))

        print(inst_list)

    def do_update(self, arg):
        """Updates instances based on class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]

        if cls_name not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        inst_id = args[1]
        insts = storage.all()
        key = "{}.{}".format(cls_name, inst_id)

        if key not in insts:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        att_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        att_val = args[3]

        inst = insts[key]

        if att_name not in inst.__dict__:
            return

        att_type = type(inst.__dict__[att_name])

        try:
            att_value = att_type(att_val)
        except valueError:
            return

        inst.__dict__[att_name] = att_value
        inst.save()
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
