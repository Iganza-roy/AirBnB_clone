# AirBnB Clone - Console

## Description

This project is an AirBnB clone, featuring a command-line interpreter (console) that allows users to interact with and manage instances of various classes. The application includes models for User, Place, State, City, Amenity, and Review, each inheriting from a base model.

## Command Interpreter

The command interpreter allows users to perform **CRUD(create, read, update, delete)** operations on the different classes, including **creating, updating, deleting, and displaying** instances. The available classes are BaseModel, User, Place, State, City, Amenity, and Review.

## Getting Started

To start the command interpreter, follow these steps:

1. Clone the repository:

```
git clone https://github.com/your-username/AirBnB_clone.git
```

2. Navigate to the project directory:

```
cd AirBnB_clone

```

3. Run the console:

```
./console.py
``` 
## Using the command interprater
- creating and instance:
```
create BaseModel
```
- showing an instance:
```
show BaseModel <instance_id>

```
- Updating an instance:
```
update BaseModel <instance_id> <attribute_name> "<new_value>"

```
- Destroying an instance:
```
destroy BaseModel <instance_id>
```	
