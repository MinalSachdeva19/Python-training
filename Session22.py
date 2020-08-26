# CSV Module: It is specially designed to work with csv files.
import csv
import os
import datetime

dir_path = r"E:\Industrial training\Python lectures"
file_name = "BSE-BOM504067.csv"

close_price_2019 = list()
with open(os.path.join(dir_path,file_name)) as share:
    reader = csv.DictReader(share)
    print(type(reader))
    print(reader)               # <csv.DictReader object at 0x0000017A96EA6760>
    for row in reader:
        # print(type(row))
        # print(row)
        # date = datetime.datetime(row["Date"])   # Will return error - an integer is required (got type str)
        # Use striptime class to convert string to integer in date format.
        date = datetime.datetime.strptime(row["Date"], '%Y-%m-%d')
        # print(date)
        if date.year == 2019:
            close_price_2019.append(float(row["Close"]))

print("Average closing price of year 2019 is: ", sum(close_price_2019)/len(close_price_2019))

# JSON Module: Reading a JSON file:
import os
import json
dir1_path = r"E:\Industrial training\Python lectures"
file1_name = "example_2.json"

with open(os.path.join(dir1_path,file1_name)) as file:
    content_of_example = file.read()
    print(content_of_example)
    print(type(content_of_example))
    json_content = json.loads(content_of_example)
    print(type(json_content))

    for key in json_content:
        print(key)
        for sub_key in json_content[key]:
            print(sub_key)
            for sub_key2 in json_content[key][sub_key]:
                print(sub_key2)
                print("==============")
                for q1 in json_content[key][sub_key][sub_key2]:
                    print(q1)
                    print(json_content[key][sub_key][sub_key2]["answer"])

# WAP to find average closing price of year 2019 from JSON file of Quandl:
import json
import requests
import datetime

close_price_2019 = list()

url = "https://www.quandl.com/api/v3/datasets/BSE/BOM504067.json?api_key=b-H3K64ErMQNM_oTA3fn"

request_object = requests.get(url)
print(request_object)                   # <Response [200]> -> Indicating success .This class of status codes indicates the action
# requested by the client was received, understood, and accepted.
print(type(request_object))

content = request_object.text
print(content)
print(type(content))
json_content = json.loads(content)
print(content)
print(type(json_content))

print("==============")

for key in json_content:
    print(key)                  # There is only one key: dataset.
print("==============")
for data in json_content["dataset"]:
    print(data)                 # This will return keys of key(dataset).
print("==============")
for sub_data in json_content["dataset"]["data"]:
    print(sub_data)             # Date is at 0th index and close is at 4th index.
    print("="*100)
    print(sub_data[0])
    date = datetime.datetime.strptime(sub_data[0],"%Y-%m-%d")
    print(date)
    year = date.year
    if year == 2019:
        close_price_2019.append(sub_data[4])

print("Average of close price of year 2019:",sum(close_price_2019)/len(close_price_2019))


