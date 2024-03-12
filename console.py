#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines a class for the command interpreter"""

    prompt = "(hbnb) "

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing if an empty line"""
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
        """Creates a new instance of the provided class"""
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
        insts = storage.all()
        key = "{}.{}".format(args[0], args[1])

        if key not in insts:
            print("** no instance found **")
            return
        print(insts[key])

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

        inst_id = args[1]
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

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
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

        if hasattr(inst, att_name):
            att_type = type(getattr(inst, att_name))
            if att_type is str:
                att_val = str(att_val)
            elif att_type is int:
                att_val = int(att_val)
            elif att_type is float:
                att_val = float(att_val)
            elif att_type is list or att_type is dict:
                try:
                    att_val = eval(att_val)
                except Exception:
                    pass

        setattr(inst, att_name, att_val)
        inst.save()

    def default(self, other):
        """Default method for custom commands"""
        args = other.split(".")
        custom = args[1]
        if len(args) == 2 and custom == "all()":
            cls_name = args[0]
            if cls_name in self.__classes:
                self.do_all(cls_name)
                return
        elif len(args) == 2 and custom == "count()":
            cls_name = args[0]
            if cls_name in self.__classes:
                count = sum(1 for obj in storage.all().keys() if obj.split('.')[0] == cls_name)
                print(count)
                return

        return super().default(other)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
