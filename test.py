from main import documents, directories, people_output, add_document, delete_document
import unittest
from unittest import mock

class TestFunctions(unittest.TestCase):

    def test_people_output(self):
        self.assertEqual(people_output(documents), 'Геннадий Покемонов')

    def test_add_document(self):
        self.assertEqual(add_document(documents, directories), documents)

    def test_delete_document(self):
        self.assertEqual(delete_document(documents, directories), documents)

if __name__ == '__main__':
    unittest.main()

