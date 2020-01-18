from settings import restore_url, headers, path_users, output_output
from base_methods import send_data, open_backup


def prepare_json(user):
    json = {
        "username": user['username'],
        "email": user['email'],
        "password": user['password']
    }
    return json


users = open_backup(output_output)
for user in users:
    data = prepare_json(user)
    send_data(restore_url + path_users, headers, data)
