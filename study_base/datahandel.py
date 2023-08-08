import json
import os


def read_file(path):
    with open(path, encoding='utf-8') as sms_txt:
        file_content = sms_txt.readlines()

    for item in file_content:
        if '>' in item:
            json_str = item[item.index(">") + 1:]
            data = json.loads(json_str)
            status_box = data['statusbox']
            handel_data(status_box)


def handel_data(status_box):
    if isinstance(status_box, dict):
        write2file(status_box)
    else:
        for item in status_box:
            write2file(item)


def write2file(item):
    status = item.get('status')
    with open(file_dict.get(str(status)), 'a', encoding='utf-8') as file_object:
        file_object.writelines(item.get('taskid') + "\n")


def recreate_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, "w")
    f.close()


file_dict = {
    "20": "E:/Users/yf/Desktop/12.txt",
    "10": "E:/Users/yf/Desktop/11.txt",
    "30": "E:/Users/yf/Desktop/13.txt",
}

if __name__ == '__main__':
    for file in file_dict:
        recreate_file(file)

    read_file("E:/Users/yf/Desktop/短信.txt")
