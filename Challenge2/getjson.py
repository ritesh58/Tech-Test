import requests
import json

instance_url = 'http://169.254.169.254/latest/'

#recursive function to parse metadata value and return dictionary
def parse_jsontree(url, arr):
    result = {}
    for item in arr:
        new_url = url + item
        r = requests.get(neiw_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            result[item[:-1]] = parse_jsontree(new_url, list_of_values)
        elif is_valid_json(text):
            result[item] = json.loads(text)
        else:
            result[item] = text
    return result

#function to return output in Dictionary
def metadata():
    path = ["meta-data/"]
    result = parse_jsontree(instance_url, path)
    return result

#function to return output in json
def metadata_json():
    md = metadata()
    metadata_json = json.dumps(md, indent=4, sort_keys=True)
    return metadata_json


def is_valid_json(value):
    try:
        json.loads(value)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(metadata_json())
                          