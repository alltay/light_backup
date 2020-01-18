from settings import backup_url, headers, path_subs, output_subs
from base_methods import send_data, open_backup


def prepare_json(sub):
    json = {
        'user': sub['user'],
        "subscription_name": sub['subscription_name'],
        "user_count": sub['user_count'],
        "subscription_till": sub['subscription_till']
    }
    return json


subs = open_backup(output_subs)
for sub in subs:
    response = send_data(
        backup_url + path_subs, headers, prepare_json(sub))
    print(response)
