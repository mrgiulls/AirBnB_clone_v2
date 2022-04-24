#!/usr/bin/python3

""" Console Module"""

import cmd

from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""
    prompt = '(hbnb)'
    intro = ""

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit """
        print("Exits the program with formatting")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Overrides the emptyline method of CMD """
        pass

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Overrides create """
        if not args:
            print("** class name missing **")
            return
        elif args != "BaseModel":
            print("** class doesn't exist")
            return
        new_instance = BaseModel()
        print(new_instance.id)

    def do_show(self, args):
        """ Show command """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if not c_name:
            print("** class name missing**")
            return

        key = c_name + "." + c_id

        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ destroy """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        
        if not c_name:
            print("** class name missing**")
            return
        if not c_id:
            print("** class id missing**")
            return

        key = c_name + "." + c_id
        try:
            del(storage.FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """ """
        if args != "BaseModel":
            print("** class doesn't exist **")
            return

        for k, v in storage._FileStorage__objects.items():
            print(v)

    def do_update(self, args):
        """ """
        new = args.split(" ")
        c_name = new[0]
        c_id = new[1]
        att_name = new [3]
        att_val = new[4]
        if not c_name:
            print("** class name missing**")
            return
        if not c_id:
            print("** class id missing **")
            return
        if not att_name:
            print("** attribute name missing **")
            return
        if att_val:
            print("** value missing **")
            return

        key = c_name + "." + c_id

        try:
            new_dict = storage._FileStorage__objects[key]
            new_dict.update({att_name: att_val})
        except KeyError:
            print ("** no instance found **")
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
