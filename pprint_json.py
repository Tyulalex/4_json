import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        return json.loads(json_file.read())


def pretty_print_json(json_content):
    print(json.dumps(json_content, indent=2))


if __name__ == '__main__':
    json_content = load_data(filepath=sys.argv[1])
    pretty_print_json(json_content)
