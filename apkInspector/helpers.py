import json


def pretty_print_header(header_text, width=50, char='-'):
    """
    Formatting output used for the CLI
    :param header_text: The text to be displayed
    :param width: total width of the display
    :param char: which char to be used as a filler
    """
    padding = max(0, width - len(header_text)) // 2
    formatted_header = f"\n{char * padding} {header_text} {char * padding}"
    print(formatted_header)


def save_data_to_file(filename, data):
    """
    Write data to file
    :param data: the actual data
    :param filename: file to be saved in
    """
    try:
        with open(filename, 'wb') as output_file:
            output_file.write(data)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error while saving data to {filename}: {e}")


def save_to_json(filename, dictionary):
    """
    Simple method to save a dictionary as JSON into the filename
    :param filename: the name of the file to be saved as
    :param dictionary: the dictionary to be saved as JSON
    """
    with open(filename, "w") as h_file:
        json.dump(dictionary, h_file, indent=4)