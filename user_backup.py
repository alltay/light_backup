from settings import backup_url, headers, path_users, output_users
from base_methods import get_data, save_backup, prepare_output


response = get_data(backup_url + path_users, headers)
save_backup(prepare_output(response)[1:], output_users)
if response['next'] is not None:
    response = get_data(response['next'], headers)
    print(response)
