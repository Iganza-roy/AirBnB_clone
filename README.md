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

## Example:
```
root@416340e4278d:/AirBnB_clone# ./console.py
(hbnb) create BaseModel
1ffd2865-850d-4caf-a89d-1826411cc7c1
(hbnb) all BaseModel
["[BaseModel] (ff2d517f-d0cd-4973-a4e5-0a7bc7dbe12b) <{'id': 'ff2d517f-d0cd-4973-a4e5-0a7bc7dbe12b', 'created_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 357917), 'updated_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 357919)}>", "[BaseModel] (a4a20999-effa-45b5-b561-cf5fda990be1) <{'id': 'a4a20999-effa-45b5-b561-cf5fda990be1', 'created_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 358030), 'updated_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 358031)}>", "[BaseModel] (b82051d1-ce23-43ef-833e-790287550221) <{'id': 'b82051d1-ce23-43ef-833e-790287550221', 'created_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 358563), 'updated_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 358564)}>", "[BaseModel] (1ffd2865-850d-4caf-a89d-1826411cc7c1) <{'id': '1ffd2865-850d-4caf-a89d-1826411cc7c1', 'created_at': datetime.datetime(2024, 3, 9, 11, 27, 5, 82855), 'updated_at': datetime.datetime(2024, 3, 9, 11, 27, 5, 82875)}>"]
(hbnb) update BaseModel 1ffd2865-850d-4caf-a89d-1826411cc7c1 first_name "Betty"
(hbnb) show BaseModel 1ffd2865-850d-4caf-a89d-1826411cc7c1
[BaseModel] (1ffd2865-850d-4caf-a89d-1826411cc7c1) <{'id': '1ffd2865-850d-4caf-a89d-1826411cc7c1', 'created_at': datetime.datetime(2024, 3, 9, 11, 27, 5, 82855), 'updated_at': datetime.datetime(2024, 3, 9, 11, 27, 5, 82875)}>
(hbnb) all BaseModel
["[BaseModel] (ff2d517f-d0cd-4973-a4e5-0a7bc7dbe12b) <{'id': 'ff2d517f-d0cd-4973-a4e5-0a7bc7dbe12b', 'created_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 357917), 'updated_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 357919)}>", "[BaseModel] (a4a20999-effa-45b5-b561-cf5fda990be1) <{'id': 'a4a20999-effa-45b5-b561-cf5fda990be1', 'created_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 358030), 'updated_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 358031)}>", "[BaseModel] (b82051d1-ce23-43ef-833e-790287550221) <{'id': 'b82051d1-ce23-43ef-833e-790287550221', 'created_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 358563), 'updated_at': datetime.datetime(2024, 3, 9, 11, 9, 26, 358564)}>", "[BaseModel] (1ffd2865-850d-4caf-a89d-1826411cc7c1) <{'id': '1ffd2865-850d-4caf-a89d-1826411cc7c1', 'created_at': datetime.datetime(2024, 3, 9, 11, 27, 5, 82855), 'updated_at': datetime.datetime(2024, 3, 9, 11, 27, 5, 82875)}>"]
(hbnb) destroy BaseModel 1ffd2865-850d-4caf-a89d-1826411cc7c1
(hbnb) show BaseModel 1ffd2865-850d-4caf-a89d-1826411cc7c1
** no instance found **
(hbnb) 
```	
