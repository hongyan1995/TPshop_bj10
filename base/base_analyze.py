import yaml


def analyze_data(file_name, case_key):
    with open("./data/" + file_name + ".yaml", "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)[case_key]
        data_list = list()
        data_list.extend(data.values())
        return data_list
