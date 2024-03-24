#!/usr/bin/python3

""" console """

import sys
import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):

    """ commmands  """
    prompt = '(hbnb) '

    def do_quit(self, line):

        """ quit: exits the program """

        sys.exit()

    def do_EOF(self, line):

        """ exits the program """

        return True

    def help_quit(self):

        """ help for quit """

        print("\n[quit]: exits the program\n")

    def emptyline(self):

        """ does nothing if line empty """

        pass

    def check_id(self, id):

        """ checks id """

        try:
            rand = storage.all()[id]
        except KeyError:
            print("** no instance found **")
            return False
        else:
            return True

    def do_create(self, line):

        """ creates and saves instance of the model """

        models = {'BaseModel': BaseModel,
                  'User': User, 'Place': Place,
                  'State': State, 'Amenity': Amenity,
                  'City': City, 'Review': Review
                  }
        models_name = ['BaseModel', 'User', 'State',
                       'City', 'Amenity', 'Place',
                       'Review']
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) > 1 or args[0] not in models:
            print("** class doesn't exist **")
        else:
            new = models[args[0]]()
            new.save()
            print(new.id)

    def do_show(self, line):

        """ prints the string representation of an instance
            based on class name and id
        """
        models = ['BaseModel', 'User', 'State', 'City',
                  'Amenity', 'Place', 'Review']
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) > 2:
            print("** no instance found **")
        else:
            key = f'{args[0]}.{args[1]}'
            if self.check_id(key):
                print(storage.all()[key])

    def do_destroy(self, line):

        """ Deletes obj from  storage """

        models = ['BaseModel', 'User', 'State', 'City',
                  'Amenity', 'Place', 'Review']
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) > 2:
            print("** no instance found **")
        else:
            key = f'{args[0]}.{args[1]}'
            if self.check_id(key):
                del storage.all()[key]
                storage.save()

    def do_all(self, line):

        """ prints out all string representation  """

        st = storage.all()
        base_id = []
        user_id = []
        state_id = []
        city_id = []
        amenity_id = []
        place_id = []
        review_id = []

        for id in st:
            if id.split(".")[0] == "User":
                user_id.append(id)
            elif id.split(".")[0] == "BaseModel":
                base_id.append(id)
            elif id.split(".")[0] == "State":
                state_id.append(id)
            elif id.split(".")[0] == "City":
                city_id.append(id)
            elif id.split(".")[0] == "Amenity":
                amenity_id.append(id)
            elif id.split(".")[0] == "Place":
                place_id.append(id)
            elif id.split(".")[0] == "Review":
                review_id.append(id)

        b_id = [st[ids].__str__() for ids in base_id]
        u_id = [st[ids].__str__() for ids in user_id]
        s_id = [st[ids].__str__() for ids in state_id]
        c_id = [st[ids].__str__() for ids in city_id]
        a_id = [st[ids].__str__() for ids in amenity_id]
        p_id = [st[ids].__str__() for ids in place_id]
        r_id = [st[ids].__str__() for ids in review_id]

        all_model = b_id + u_id + s_id + c_id + a_id + p_id + r_id

        if len(line.split()) == 0:
            print(all_model)

        elif len(line.split()) > 1:
            print("** class doesn't exis**")

        elif line.split()[0] == 'BaseModel':
            print(b_id)
        elif line.split()[0] == 'User':
            print(u_id)
        elif line.split()[0] == 'State':
            print(s_id)
        elif line.split()[0] == 'City':
            print(c_id)
        elif line.split()[0] == 'Amenity':
            print(a_id)
        elif line.split()[0] == 'Place':
            print(p_id)
        elif line.split()[0] == 'Review':
            print(r_id)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):

        """ updates an object attr """

        args = line.split()
        models = ['BaseModel', 'User', 'State', 'City',
                  'Amenity', 'Place', 'Review']
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = f'{args[0]}.{args[1]}'
            if self.check_id(key):
                update = storage.all()[key]
                value = args[3]
                if value.isdigit():
                    value = int(value)
                elif '.' in value:
                    check = value.replace('.', '', 1)
                    if check.isdigit():
                        value = float(value)
                else:
                    value = value

                var = args[2]
                data = value
                setattr(update, var, data)
                update.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
