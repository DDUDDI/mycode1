import json
import os.path
mempath = 'D:/Pycharm_Projects/0518/선생님/memDic.txt'


def line2dic(line):
    info = line.split()
    dic = {}
    dic['num'] = int(info[0])
    dic['name'] = info[1]
    dic['phone'] = info[2]
    return dic

def dic_from_json():
    if not os.path.isfile(mempath): # file이 없는 경우
        with open(mempath, 'w') as f: # write를 위해 신규 file 생성
            json.dump([], f) # 빈 list를 file에 입력(list->json string)
    with open(mempath) as f:
        content = json.load(f)
    return content

def list2jsonfile(memList):
    with open(mempath, 'w') as f:
        json.dump(memList, f)

def add(dic):
    memList = dic_from_json()
    memList.append(dic)
    list2jsonfile(memList)

def find_name(name):
    memList = dic_from_json()
    for d in memList:
        if d['name'] == name:
            return d
    return None

def update(name, phone):
    memList = dic_from_json()
    for d in memList:
        if d['name'] == name:
            d['phone'] = phone
        break
    list2jsonfile(memList)

def delete(name):
    memList = dic_from_json()
    for d in memList:
        if d['name'] == name:
            memList.remove(d)
        break
    list2jsonfile(memList)