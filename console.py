#!/usr/bin/python3

""" console """

import sys
import cmd
from models.base_model import BaseModel
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

    def check_line_model(self, line):
        
        """ checks the lines and returns appropriate"""
        args = line.split()
        models = ('BaseModel', 'User')
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) > 0:
            if args[0] not in models:
                print("** class doesn't exist **")
            else:
                return args[0]

    def check_line_id(self, line):

        if self.check_line_model(line):
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
            else:
                return True

    def check_id(self, id):

        try:
            rand = storage.all()[id]
        except KeyError:
            print("** no instance found **")
            return False
        else:
            return True
            

    def do_create(self, line):

        """ creates and saves instance of the model """
        if self.check_line_model(line) == 'BaseModel':
            new = BaseModel()
            new.save()
            print(new.id)

        elif self.check_line_model(line) == "User":
            new = User()
            new.save()
            print(new.id)

    def do_show(self, line):

        """ prints the string representation of an instance
            based on class name and id
        """
        args = line.split()
        if self.check_line_id(line):
            id = self.check_line_model(line)
            key = f'{id}.{args[1]}'
            if self.check_id(key):
                if id == 'BaseModel':
                    base = BaseModel()
                    storage_ins = storage.all()[key]
                    base_model = BaseModel(**storage_ins)
                    print(base_model)
                elif id == 'User':
                    base = User()
                    storage_ins = storage.all()[key]
                    user_model = User(**storage_ins)
                    print(user_model)


    def do_destroy(self, line):
        
        args = line.split()
        if self.check_line_id(line):
            key = self.check_line_model(line)
            id = f'{key}.{args[1]}'
            if self.check_id(id):
                del storage.all()[id]
                storage.save()

    def do_all(self, line):

            st = storage.all()
            base_id = []
            user_id = []
            for id in st:
                if id.split(".")[0] == "User":
                    user_id.append(id)
                elif id.split(".")[0] == "BaseModel":
                    base_id.append(id)
            b_id = [BaseModel(**st[ids]).__str__() for ids in base_id]
            u_id = [User(**st[ids]).__str__() for ids in user_id]
            all_model = b_id + u_id
            
            if len(line.split()) == 0:
                print(all_model)

            elif line.split()[0] == 'BaseModel':
                print(b_id)
            elif line.split()[0] == 'User':
                print(u_id)
            else:
                print("** class doesn't exist **")
                        

    def do_update(self, line):

        args = line.split()
        if self.check_line_id(line):
            key = self.check_line_model(line)

            id = f'{key}.{args[1]}'
            if self.check_id(id):
                if len(args) == 2:
                    print("** attribute name missing **")

                elif len(args) == 3:
                    print("** value missing **")
                else:
                    update = storage.all()[id]
                    value = args[3]
                    if value.isdigit():
                        value = int(value)
                    elif '.' in value:
                        check = value.replace('.', '', 1)

                        if check.isdigit():
                            value = float(value)
                    else:
                        value = value

                    update[args[2]] = str(value)
                    storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
