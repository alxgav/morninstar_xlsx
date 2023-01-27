


def add_to_list(data_list: list, length: int) -> list:
    while('-' in data_list):
        data_list.remove('-')
    length_cr = len(data_list)
    if length_cr < length:
        for item in range(length - length_cr):
            data_list = [float("NaN")] + data_list
    return data_list