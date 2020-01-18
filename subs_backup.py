from settings import backup_url, headers, path_subs, output_subs
from base_methods import get_data, save_backup, prepare_output


response = get_data(backup_url + path_subs, headers)
output = prepare_output(response)
if response['next'] is not None:
    response = get_data(response['next'], headers)
    output += prepare_output(response)
save_backup(output, output_subs)
print("Saved: %s items" % len(output))
