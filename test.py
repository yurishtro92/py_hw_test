from main import documents, directories, people_output, add_document, delete_document
import unittest.mock

class TestFunctions(unittest.TestCase):
    @unittest.mock.patch('builtins.input', side_effect=['11-2'])
    def test_people_output(self, mock):
        self.assertEqual(people_output(documents), "Геннадий Покемонов")

    @unittest.mock.patch('builtins.input', side_effect=['1', 'passport', 'mr.Noname', '1'])
    def test_add_document(self, mock):
        self.assertEqual(add_document(documents, directories), ('1', 'passport', 'mr.Noname', '1'))

    @unittest.mock.patch('builtins.input', side_effect=['1'])
    def test_delete_document(self, mock):
        self.assertEqual(delete_document(documents, directories), True)

if __name__ == '__main__':
    unittest.main()



