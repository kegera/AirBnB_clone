#!/usr/bin/python3

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
    def do_nothing(self, arg):
        """no change"""
        pass

    def do_EOF(self, arg):
        """exit program upon end of file"""
        print("")
        return True

    def do_create(self, arg):
        """new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        x_data = shlex.split(arg)
        if (x_data[0] not in HBNBCommand.mods.keys()):
            print("** class doesn't exist **")
            return
        base_instance = HBNBCommand.mods[x_data[0]]()
        base_instance.save()
        print(base_instance.id)

    def do_show(self, arg):
        """display the string representation"""
        args = shlex.split(arg)
        if (len(args) == 0):
            print("** class name missing **")
            return
        if (args[0] not in HBNBCommand.mods.keys()):
            print("** class doesn't exist **")
            return
        if (len(args) <= 1):
            print("** instance id missing **")
            return
        models.storage.reload()
        objs = models.storage.all()
        obj_key = args[0] + "." + args[1]
        if (obj_key in objs):
            insts = str(objs[obj_key])
            print(insts)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """delete a specific instance"""
        args = shlex.split(arg)
        if (len(args) == 0):
            print("** class name missing **")
            return
        if (args[0] not in HBNBCommand.mods.keys()):
            print("** class doesn't exist **")
            return
        if (len(args) <= 1):
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
        jfile = []
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
            print("** class doesn't exist **")

    def do_count(self, arg):
        """counts how many instances a class has"""
        c = 0
        obj_dict = models.storage.all()
        for k in obj_dict:
            if (arg in k):
                c += 1
        print(c)

    def do_update(self, arg):
        """update an isntance"""
        models.storage.reload()
        obj_dict = models.storage.all()
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if (args[0] not in HBNBCommand.mods.keys()):
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
                "destory": self.do_destroy,
                "show": self.do_show,
                "update": self.do_update
                }
        args = arg.strip()
        v = arg.split(".")
        if (len(v) != 2):
            cmd.Cmd.default(self, arg)
            return
        cl_name = v[0]
        cmds = v[1].split("(")[0]
        l = ""
        if (cmds == "update" and v[1].split("(")[1][-2] == "}"):
            inp = v[1].split("(").split(",", 1)
            inp[0] = shlex.split(inp[0])[0]
            l = "".join(inp)[0:-1]
            l = cl_name + " " + l
            delf.do_update(l.strip())
            return
        try:
            inp = v[1].split("(")[1].split(",")
            for n in range(len(inp)):
                if (n != len(inp) -1):
                    l = l + " " + shlex.split(inp[n])[0]
                else:
                    l = l + " " + shlex.split(inp[n][0:-1])[0]
        except IndexError:
            inp = ""
            l = ""
            l = cl_name + l
            if (cmds in y_dict.keys()):
                y_dict[cmds](l.strip())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
