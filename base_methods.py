import json
import requests


def get_data(url, headers):
    """
        1. Get url and headers;
        2. Make get request;
        3. Return response text.
    """
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 'error %s' % response.status_code
    else:
        return json.loads(response.text)


def send_data(url, headers, data):
    """
        1. Get url and headers and json;
        2. Make post response;
        3. Return response text.
    """
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 201:
        return 'error %s' % response.status_code
    else:
        return json.loads(response.text)


def prepare_output(response):
    """
        1. Get response in json;
        2. Return new json output.
    """
    output = []
    for item in response['results']:
        output.append(item)
    return output


def open_backup(file):
    """
        1. Get file name/path;
        2. Return data in json.
    """
    with open(file, 'r') as f:
        data = f.read()
    return json.loads(data)


def save_backup(output, file):
    """
        1. Get json data, file name/path;
        2. Save data to file.
    """
    with open(file, 'w') as f:
        f.write(json.dumps(output))
