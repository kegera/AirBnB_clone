#!/usr/bin/python3

"""Defines AirBnB console"""
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    mods = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def emptyline(self):
        """empty line"""
        pass

    def do_quit(self, arg):
        """quit the program"""
        return True

    def do_EOF(self, arg):
        """exit program upon end of file"""
        print("")
        return True

    def do_create(self, arg):
        """new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        x_data = shlex.split(arg)
        if (x_data[0] not in HBNBCommand.mods.keys()):
            print("** class doesn't exist **")
        base_instance = HBNBCommand.mods[x_data[0]]()
        models.storage.save()
        print(base_instance.id)

    def do_show(self, arg):
        """display the string representation"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        models.storage.reload()
        args_dict = models.storage.all()
        args_key = args[0] + "." + args[1]
        if args_key in args_dict:
            args_inst = str(args_dict[args_key])
            print(args_inst)
        else:
            print("** no instance found **")
            
        """nme, argsid = None, None
        if (len(args) > 0):
            nme = args[0]
        if len(args) > 1:
            argsid = args[1]
        if not nme:
            print("** class name missing **")
        elif not argsid:
            print("** instance id missing **")
        elif (args[0] not in HBNBCommand.mods.keys()):
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            obj_key = nme + "." + argsid
            objs = models.storage.all().get(obj_key)
            if (obj_key in objs):
                print(objs)
            else:
                print("** no instance found **") """

    def do_destroy(self, arg):
        """delete a specific instance"""
        args = shlex.split(arg)
        if (len(args) == 0):
            print("** class name missing **")
            return
        if (args[0] not in HBNBCommand.mods):
            print("** class doesn't exist **")
            return
        if (len(args) == 1):
            print("** instance id missing **")
            return
        models.storage.reload()
        objs = models.storage.all()
        obj_key = args[0] + "." + args[1]
        if (obj_key in objs):
            del objs[obj_key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """display all instances"""
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
        else:
            jfile = []
            for obj in models.storage.all():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    jfile.append(obj.__str__())
                elif len(args) == 0:
                    jfile.append(obj.__str__())
            print(jfile)
        """jfile = []
        args = shlex.split(arg)
        models.storage.reload()
        obj_dict = models.storage.all()
        if not arg:
            for k in obj_dict:
                jfile.append(str(obj_dict[k]))
            print(json.dumps(jfile))
            return
        if (args[0] in HBNBCommand.mods.keys()):
            for k in obj_dict:
                if args[0] not in k:
                    jfile.append(str(obj_dict[k]))
            print(json.dumps(jfile))
        else:
            print("** class doesn't exist **")"""

    def do_count(self, arg):
        """counts how many instances a class has"""
        c = 0
        obj_dict = models.storage.all()
        for k in obj_dict:
            if arg == k.split(".")[0]:
                c += 1
        print(c)

    def do_update(self, arg):
        """update an isntance"""
        args = shlex.split(arg)
        models.storage.reload()
        obj_dict = models.storage.all()
        if not args:
            print("** class name missing **")
            return
        if (args[0] not in HBNBCommand.mods):
            print("** class doesn't exist **")
            return
        if (len(args) == 1):
            print("** instance id missing **")
            return

        try:
            obj_key = args[0] + "." + args[1]
            obj_dict[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(args) == 2):
            print("** attribute name missing **")
            return
        if (len(args) == 3):
            print("** value missing **")
            return
        if (hasattr(obj_dict[obj_key], args[2])):
            typeval = type(getattr(obj_dict[obj_key], args[2]))
            setattr(obj_dict[obj_key], args[2], typeval(args[3]))
        else:
            setattr(obj_dict[obj_key], args[2], args[3])
        models.storage.save()

    def default(self, arg):
        """more ways of data input"""
        y_dict = {
                "count": self.do_count,
                "all": self.do_all,
                "destroy": self.do_destroy,
                "show": self.do_show,
                "update": self.do_update
                }
        args = arg.strip().split(".")
        if (len(args) != 2):
            cmd.Cmd.default(self, arg)
            return
        cl_name, cmds = args
        cmds, params = cmds.split("(", 1)
        if cmds == "update" and params.endswith("}"):
            params = params[:-1]
        elif cmds in y_dict:
            if cmds in ["all", "count"]:
                cl_name = cl_name if cmds == "all" else ""
            y_dict[cmds](f"{cl_name} {params}")
        else:
            cmd.Cmd.default(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
