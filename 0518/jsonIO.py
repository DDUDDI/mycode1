import json
import os.path

filepath = 'D:/Pycharm_Projects/0518/json.txt'

# 키보드로 입력 받은 정보 -> dic
def line2dic(line):
    info = line.split()
    dic = {}
    dic['num'] = info[0]
    dic['name'] = info[1]
    dic['phone'] = info[2]
    return dic

# json -> list
def list_from_json():
    if not os.path.isfile(filepath): # filepath에 file이 없는 경우
        with open(filepath, 'w') as f: # filepath에 신규 file write
            json.dump([], f)
    with open(filepath) as f:
        content = json.load(f)
    return content

# list -> json
def list2json(memList):
    with open(filepath, 'w') as f:
        json.dump(memList, f)

def add(dic):
    memList = list_from_json()
    memList.append(dic)
    list2json(memList)

def findname(name):
    memList = list_from_json()
    for m in memList:
        if m['name'] == name:
            return m
    return None

def update(name, phone):
    memList = list_from_json()
    for m in memList:
        if m['name'] == name:
            m['phone'] = phone
        break
    list2json(memList)

def delete(name):
    memList = list_from_json()
    for m in memList:
        if m['name'] == name:
            memList.remove(m)
        break
    list2json(memList)
