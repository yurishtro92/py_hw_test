import requests
token_ydisk = 'token'
token_ydisk_crushed = 'invalid_token'

def create_folder():
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'OAuth {}'.format(token_ydisk)}
    params = {"path": 'New folder'}
    response = requests.put(upload_url, headers=headers, params=params)
    return response.status_code

def create_folder_conflict_exists_path():
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'OAuth {}'.format(token_ydisk)}
    params = {"path": 'New folder'}
    response = requests.put(upload_url, headers=headers, params=params)
    return response.status_code

def create_folder_token_crushed():
    upload_url1 = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'OAuth {}'.format(token_ydisk_crushed)}
    params1 = {"path": 'New folder'}
    response = requests.put(upload_url1, headers=headers, params=params1)
    return response.status_code
