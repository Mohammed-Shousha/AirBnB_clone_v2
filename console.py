#!/usr/bin/python3
"""HBNB Console Implementation"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import warnings
warnings.filterwarnings("ignore")


def parse(arg):
    """Parses arguments from line"""
    import re
    from shlex import split
    curly_braces_content = re.search(r"\{(.*?)\}", arg)
    brackets_content = re.search(r"\[(.*?)\]", arg)

    # Choose the first match found, or None if neither is found
    match = curly_braces_content or brackets_content

    if match is None:
        return [item.strip(",") for item in split(arg)]
    else:
        # Split the part of arg before the matched braces or brackets
        lexer = split(arg[:match.span()[0]])

        # Remove trailing commas from each substring in lexer
        items_without_commas = [item.strip(",") for item in lexer]

        # Append the matched braces or brackets content
        items_without_commas.append(match.group())

        return items_without_commas


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class """

    prompt = '(hbnb) '

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        command_to_method = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        command_parts = arg.split('.', 1)
        if len(command_parts) == 2:
            class_name, command_with_args = command_parts
            command_name, _, args = command_with_args.partition('(')
            args = args.rstrip(')')

            if command_name in command_to_method:
                call = "{} {}".format(class_name, args)
                return command_to_method[command_name](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything"""
        pass

    def _parse_params(self, params):
        params_dict = {}
        for param in params:
            key, value = param.split("=")
            value = value.replace("_", " ")

            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1]
            elif "." in value:
                value = self._try_parse_float(value)
            else:
                value = self._try_parse_int(value)

            params_dict[key] = value
        return params_dict

    def _try_parse_float(self, value):
        try:
            return float(value)
        except ValueError:
            return value

    def _try_parse_int(self, value):
        try:
            return int(value)
        except ValueError:
            return value

    def do_create(self, arg):
        """
        Usage: create <class>
        Creates a new instance of a given class
        """
        command_args = parse(arg)

        if not command_args:
            return print("** class name missing **")

        class_name = command_args[0]
        if class_name not in self.__classes:
            return print("** class doesn't exist **")

        if command_args == 1:
            new_instance = self.__classes[class_name]()
            new_instance.save()
            return print(new_instance.id)

        params = command_args[1:]
        params_dict = self._parse_params(params)

        new_instance = self.__classes[class_name](**params_dict)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Usage: show <class> <id>
        Prints the string representation of an instance
        based on the class name and id
        """
        if len(arg) == 0:
            return print("** class name missing **")

        args = parse(arg)
        if args[0] not in self.__classes.keys():
            return print("** class doesn't exist **")

        if len(args) == 1:
            return print("** instance id missing **")

        key = args[0] + "." + args[1]
        if key not in storage.all():
            return print("** no instance found **")

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Usage: destory <class> <id>
        Deletes an instance based on the class name and id
        """
        if len(arg) == 0:
            return print("** class name missing **")

        args = parse(arg)
        if args[0] not in self.__classes.keys():
            return print("** class doesn't exist **")

        if len(args) == 1:
            return print("** instance id missing **")

        key = args[0] + "." + args[1]
        if key not in storage.all():
            return print("** no instance found **")

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Usage: all or all <class>
        Prints all string representation of all
        instances based or not on the class name
        """
        if len(arg) == 0:
            return print([str(x) for x in storage.all().values()])

        args = parse(arg)
        if args[0] not in self.__classes.keys():
            return print("** class doesn't exist **")

        print([str(v) for v in storage.all().values()
               if v.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """
        Usage: update <class> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name
        and id by adding or updating an attribute
        """

        if len(arg) == 0:
            return print("** class name missing **")

        args = parse(arg)
        for i in range(3):
            args[i] = str(args[i])

        if "num" in args[3] or "number" in args[3]:
            args[3] = int(args[3])
        else:
            args[3] = str(args[3])

        if args[0] not in self.__classes.keys():
            return print("** class doesn't exist **")

        if len(args) == 1:
            return print("** instance id missing **")

        key = args[0] + "." + args[1]
        if key not in storage.all():
            return print("** no instance found **")

        if len(args) == 2:
            return print("** attribute name missing **")

        if len(args) == 3:
            return print("** value missing **")

        storage_objs = storage.all()

        setattr(storage_objs[key], args[2], args[3])
        storage_objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
