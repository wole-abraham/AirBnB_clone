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

    def check_line_model(self, line):
        
        """ checks the lines and returns appropriate"""
        args = line.split()
        retVal = ''
        models = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
        if len(args) == 0:
            retVal = f"** class name missing **"
        elif len(args) == 1:
            if args[0] not in models:
                retVal = f"** class doesn't exist **"
            else:
                retVal = args[0]
        else:
            retVal = f"** class doesn't exist **"
                
        return retVal

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

        elif self.check_line_model(line) == 'State':
            new = State()
            new.save()
            print(new.id)

        elif self.check_line_model(line) == 'City':
            new = City()
            new.save()
            print(new.id)

        elif self.check_line_model(line) == 'Amenity':
            new = Amenity()
            new.save()
            print(new.id)

        elif self.check_line_model(line) == 'Place':
            new1 = Place()
            new1.save()
            print(new1.id)

        elif self.check_line_model(line) == 'Review':
            new = Review()
            new.save()
            print(new.id)
        else:
            print(self.check_line_model(line))
    
    def do_show(self, line):

        """ prints the string representation of an instance
            based on class name and id
        """
        args = line.split()
        if self.check_line_id(line):
            id = self.check_line_model(args[0])
            key = f'{id}.{args[1]}'
            if self.check_id(key):
                if id == 'BaseModel':
                    storage_ins = storage.all()[key]
                    base_model = BaseModel(**storage_ins)
                    print(base_model)
                elif id == 'User':
                    storage_ins = storage.all()[key]
                    user_model = User(**storage_ins)
                    print(user_model)

                elif id == 'State':
                    storage_ins = storage.all()[key]
                    user_model = State(**storage_ins)
                    print(user_model)

                elif id == 'City':
                    storage_ins = storage.all()[key]
                    user_model = City(**storage_ins)
                    print(user_model)

                elif id == 'Amenity':
                    storage_ins = storage.all()[key]
                    user_model = Amenity(**storage_ins)
                    print(user_model)

                elif id == 'Place':
                    storage_ins = storage.all()[key]
                    user_model = Place(**storage_ins)
                    print(user_model)

                elif id == 'Review':
                    storage_ins = storage.all()[key]
                    user_model = Review(**storage_ins)
                    print(user_model)

    def do_destroy(self, line):
        
        args = line.split()
        if self.check_line_id(line):
            key = self.check_line_model(args[0])
            id = f'{key}.{args[1]}'
            if self.check_id(id):
                del storage.all()[id]
                storage.save()

    def do_all(self, line):

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

            b_id = [BaseModel(**st[ids]).__str__() for ids in base_id]
            u_id = [User(**st[ids]).__str__() for ids in user_id]
            s_id = [State(**st[ids]).__str__() for ids in state_id]
            c_id = [City(**st[ids]).__str__() for ids in city_id]
            a_id = [Amenity(**st[ids]).__str__() for ids in amenity_id]
            p_id = [Place(**st[ids]).__str__() for ids in place_id]
            r_id = [Review(**st[ids]).__str__() for ids in review_id]

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

        args = line.split()
        if self.check_line_id(line):
            key = self.check_line_model(args[0])

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
                        BaseModel(**update)
                        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
