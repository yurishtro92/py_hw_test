from disk_api_functions import create_folder, create_folder_token_crushed, create_folder_conflict_exists_path
import unittest

class TestYandexDisk(unittest.TestCase):

    def test_create_folder(self):
        self.assertEqual(create_folder(), 201)

    def test_create_folder_conflict_exists_path(self):
        self.assertEqual(create_folder_conflict_exists_path(), 409)

    def test_create_folder_token_crushed(self):
        self.assertEqual(create_folder_token_crushed(), 401)

if __name__ == '__main__':
    unittest.test_api()








