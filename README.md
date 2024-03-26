# AirBnB Clone 

# Using The Console

The AirBnB Clone Console is a command-line interface (CLI) tool for managing instances of various classes in the AirBnB clone project. It provides commands for creating, displaying, updating, and deleting instances of different models such as `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, and `Review`.

## Installation

1. Clone the repository:
- `git clone https://github.com/wole-abraham/AirBnB_clone/`


2. Navigate to the directory containing the console:
- `cd AirBnB_clone` 

3. Run the console: `./console.py`


## Usage

Once the console is running, you can use the following commands:

### General Commands

- `quit`: Exit the console.
- `EOF`: Exit the console (Ctrl+D).

### Model-Specific Commands

- `create <class_name>`: Create a new instance of the specified class.
- `show <class_name> <id>`: Show the string representation of an instance based on the class name and ID.
- `destroy <class_name> <id>`: Delete an instance based on the class name and ID.
- `all [class_name]`: Show all instances of a specific class or all instances if no class name is provided.
- `update <class_name> <id> <attribute_name> "<attribute_value>"`: Update an attribute of an instance based on the class name, ID, attribute name, and attribute value.

### Examples

- To create a new `User` instance:
  `create User`

- To show the details of a `User` instance with ID `1234`:
  - `show User 1234`
  
- To delete a `User` instance with the ID `1234`:
  - `destroy User 1234`
  
