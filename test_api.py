import requests
import unittest
token_ydisk = 'AQAAAAAS8cU9AADLWzuaBCrQvkqqn6J-xJpSpU0'

class TestFunctions(unittest.TestCase):

    def test_create_folder(self):
        upload_url_0 = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token_ydisk)}
        params = {"path": 'New folder'}
        response = requests.put(upload_url_0, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 201:
            print('New folder successfully created on Yandex.Disk')
        else:
            print(response.status_code)
        return response.json()

    def test_create_folder_mistake_409_folder_exists(self):
        upload_url_0 = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token_ydisk)}
        params = {"path": 'New folder'}
        response = requests.put(upload_url_0, headers=headers, params=params)
        if response.status_code == 409:
            return print('New folder exists on Yandex.Disk!')
        else:
            return print(response.status_code)

    def test_create_folder_mistake_401_unathorized(self):
        upload_url_0 = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token_ydisk)}
        params = {"path": 'New folder'}
        response = requests.put(upload_url_0, headers=headers, params=params)
        if response.status_code == 401:
            return print('Unathorized!')
        else:
            return print(response.status_code)

if __name__ == '__main__':
    unittest.test_api()


