import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        return json.loads(json_file.read())


def pretty_print_json(json_content):
    print(json.dumps(json_content, indent=2))


if __name__ == '__main__':
    raw_file_path = None
    try:
        raw_file_path = sys.argv[1]
        json_content = load_data(filepath=raw_file_path)
    except IndexError:
        print("Please enter correct path to the json file. Example of launch python pprint_json.py <Path to json>")
        sys.exit(1)
    except FileNotFoundError:
        print("The provided file {} not found. Please check if this path is correct and retry".format(raw_file_path))
        sys.exit(1)
    except json.decoder.JSONDecodeError:
        print("The provided file {} is not a json file. Please check and retry".format(raw_file_path))
        sys.exit(1)
    pretty_print_json(json_content)
