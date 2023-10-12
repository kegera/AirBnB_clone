**# AirBnB Clone - The Console**

**## Project Description**

This project is a part of the AirBnB clone series and focuses on building a **command-line interpreter** to manage AirBnB objects. This initial step is crucial as it lays the foundation for the subsequent projects, including HTML/CSS templating, database storage, API integration, and front-end development.

**## Project Details**

- **Team:** **Caleb Kegera**
- **John Mwanyasi**
- **Project Start:** October 9, 2023, 6:00 AM
- **Project End:** October 16, 2023, 6:00 AM

**## Project Objectives**

**### Concepts to Explore:**
- Python packages
- AirBnB clone

**### Project Goals:**
- Implement a parent class (**BaseModel**) for object initialization, serialization, and deserialization.
- Establish a serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> File
- Create classes for AirBnB objects (**User**, **State**, **City**, **Place**, etc.) inheriting from **BaseModel**.
- Develop the first abstracted storage engine: File storage.
- Create unit tests to validate all classes and the storage engine.

**## What's a Command Interpreter?**

The command interpreter in this project is similar to a shell but limited to managing specific objects. It allows you to:

- Create new objects (e.g., **User**, **Place**)
- Retrieve objects from files or databases
- Perform operations on objects (count, compute stats, etc.)
- Update object attributes
- Delete objects

**## Learning Objectives**

Upon completing this project, you should understand:

- How to create a Python package
- Building a command interpreter in Python using the **cmd** module
- Implementing unit testing in a large project
- Serializing and deserializing a Class
- Reading and writing JSON files
- Managing datetime in Python
- Utilizing UUID (Universally Unique Identifier)
- Working with **\*args** and **\*\*kwargs**
- Handling named arguments in functions

**## How to Start the Command Interpreter**

To start the command interpreter, follow these steps:

1. Clone the GitHub repository:
git clone https://github.com/mwanyambu/AirBnB_clone.git

2. Navigate to the project directory:
cd AirBnB_clone

3. Run the console:
./console.py

**## How to Use the Command Interpreter**

Once the console is running, you can use the following commands:

- **create <class>**: Creates a new instance of the specified class.
- **show <class> <id>**: Displays the object with the given ID of the specified class.
- **destroy <class> <id>**: Deletes the object with the given ID of the specified class.
- **all <class>**: Displays all objects of the specified class.
- **update <class> <id> <attribute name> "<attribute value>"**: Updates the specified attribute of the object with the given ID of the specified class.

**## Examples**

- Creating a new User object:
(hbnb) create User

- Showing a User object:
(hbnb) show User <user_id>

- Deleting a User object:
(hbnb) destroy User <user_id>

**## Contributors**


**## Contributors**



**## Authors**

- **Caleb Kegera**
  - [GitHub](https://www.github.com/kegera)
  - **Email:** kegeshaddy@gmail.com

- **John Mwanyambu**
  - [GitHub](https://www.github.com/mwanyambu)
  - **Email:** johnmwanyambu@gmail.com

**## How to Generate Author List**

To generate the list of authors in your Git repository, you can use the following Bash script:
```bash
#!/bin/sh

git shortlog -se | perl -spe 's/^\s+\d+\s+//' | sed -e '/^CommitSyncScript.*$/d' > AUTHORS

Please see the [AUTHORS](AUTHORS) file for a list of contributors to this project.


