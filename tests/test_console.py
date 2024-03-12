#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place


class TestConsole(unittest.TestCase):
    """testing the console"""

    def test_help_command(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

"""     
        self.assertEqual(s, f.getvalue())

    def test_show_command_no_args(self):
        """Tests show command with no arguments"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue()
            self.assertIn("** class name missing **", output)

    def test_show_command_invalid_class(self):
        """Tests show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyClass")
            output = f.getvalue()
            self.assertIn("** class doesn't exist **", output)

    @patch('models.engine.file_storage.FileStorage')
    def test_BaseModel_all(self, mock_all):
        """Tests if all instances are retrieved (using FileStorage.all)."""
        mock_all.return_value = {"User.123": User(), "Place.456": Place()}
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        output = f.getvalue()
        self.assertTrue(output)

    def test_help_all(self):
        """Tests the help command for 'all'."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        s = 'Prints all string reps of instances\n'
        self.assertEqual(s, f.getvalue())

    def test_help_update(self):
        """Tests the help command for 'update'."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        s = 'Updates instances based on class name and id\n'
        self.assertEqual(s, f.getvalue())

    def test_help_update(self):
        """Tests the help command for 'destroy'."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        s = 'Deletes an instance based on class name and id\n'
        self.assertEqual(s, f.getvalue())

    def test_quit_command(self):
        """Tests if the quit command exits the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            try:
                HBNBCommand().onecmd("quit")
            except SystemExit:
                pass

        self.assertEqual('', f.getvalue())

    def test_EOF_command(self):
        """Tests if the EOF command exits the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            try:
                HBNBCommand().onecmd("EOF")
            except SystemExit:
                pass

        self.assertEqual('\n', f.getvalue())

    def test_emptyline_method(self):
        """Tests if the emptyline method exists and doesn't raise errors."""
        console = HBNBCommand()
        self.assertTrue(hasattr(console, 'emptyline'))  # Check if the method exists
        console.emptyline()

    @patch('models.engine.file_storage.FileStorage')
    def test_update_basemodel(self, mock_all):
        """Tests updating a BaseModel instance with the update command."""
        base_model_dict = {"id": "45678", "name": "New Name"}
        mock_all.return_value = {"BaseModel.45678": BaseModel(**base_model_dict)}

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 45678 name New Name")
            output = f.getvalue()

        self.assertIn("** no instance found **\n", output)
        self.assertNotIn("AttributeError", output)

        updated_instance = mock_all.return_value["BaseModel.45678"]
        self.assertEqual(updated_instance.name, "New Name")

    @patch('models.engine.file_storage.FileStorage')
    def test_review_all(self, mock_all):
        """Tests retrieving all Review instances with Review.all()."""
        pass

    @patch('models.engine.file_storage.FileStorage')
    def test_user_all(self, mock_all):
        """Tests retrieving all user instances with user.all()"""
        pass

    @patch('models.engine.file_storage.FileStorage')
    def test_state_all(self, mock_all):
        """Tests retrieving all state instances with state.all()"""
        pass

    @patch('models.engine.file_storage.FileStorage')
    def test_amenity_all(self, mock_all):
        """Tests retrieving all amenity instances with amenity.all()"""
        pass

    @patch('models.engine.file_storage.FileStorage')
    def test_city_all(self, mock_all):
        """Tests retrieving all city instances with city.all()"""
        pass

    @patch('models.engine.file_storage.FileStorage')
    def test_place_all(self, mock_all):
        """Tests retrieving all place instances with place.all()"""
        pass


if __name__ == "__main__":
    unittest.main()
