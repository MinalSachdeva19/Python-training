# Writing data into text file from a json file:
import json
import os
import datetime
import requests

url = r"https://www.quandl.com/api/v3/datasets/BSE/SPBSN5IP.json?api_key=b-H3K64ErMQNM_oTA3fn"
February_data_2019 = list()

res_obj = requests.get(url)
content = res_obj.text
content_json = json.loads(content)

for sub_data in content_json["dataset"]["data"]:
    # print(sub_data)
    date =datetime.datetime.strptime(sub_data[0],"%Y-%m-%d")
    year = date.year
    month = date.month
    if year == 2019:
        if month == 2:
            February_data_2019.append(sub_data)

dir_path = r"E:\Industrial training\Python lectures"
file_name = "February_data_2019"

with open(os.path.join(dir_path,file_name),mode="w") as write_feb:
    for data_list in February_data_2019:
        for data_elts in data_list:
            write_feb.write(str(data_elts) + ",")
        write_feb.write("\n")

# Output in list format:
import json
import os
import datetime
import requests

url = r"https://www.quandl.com/api/v3/datasets/BSE/SPBSN5IP.json?api_key=b-H3K64ErMQNM_oTA3fn"
February_data_2019 = list()

res_obj = requests.get(url)
content = res_obj.text
content_json = json.loads(content)

for sub_data in content_json["dataset"]["data"]:
    # print(sub_data)
    date =datetime.datetime.strptime(sub_data[0],"%Y-%m-%d")
    year = date.year
    month = date.month
    if year == 2019:
        if month == 2:
            February_data_2019.append(sub_data)

dir_path = r"E:\Industrial training\Python lectures"
file_name = "February_data_2019"

with open(os.path.join(dir_path,file_name),mode="w") as write_feb:
    for data_list in February_data_2019:
        write_feb.write(str(data_list) + ",")
    write_feb.write("\n")

#  Output with column name:
import json
import os
import datetime
import requests

url = r"https://www.quandl.com/api/v3/datasets/BSE/SPBSN5IP.json?api_key=b-H3K64ErMQNM_oTA3fn"
February_data_2019 = list()

res_obj = requests.get(url)
content = res_obj.text
content_json = json.loads(content)

for sub_data in content_json["dataset"]["data"]:
    # print(sub_data)
    date =datetime.datetime.strptime(sub_data[0],"%Y-%m-%d")
    year = date.year
    month = date.month
    if year == 2019:
        if month == 2:
            February_data_2019.append(sub_data)

dir_path = r"E:\Industrial training\Python lectures"
file_name = "February_data_2019"

with open(os.path.join(dir_path,file_name),mode="w") as write_feb:
    write_feb.write(str(content_json["dataset"]["column_names"]))
    write_feb.write("\n")
    for data_list in February_data_2019:
        for data_elts in data_list:
            write_feb.write(str(data_elts) + ",")
        write_feb.write("\n")

# User defined module: Python files created by user and can be imported in any other python file as a module.
