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

if __name__ == "__main__":
    unittest.main()
