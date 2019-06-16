# _*_coding:utf-8_*_
# 项目名称 :PythonTedu 
# 作   者 : Suoha
# 文件名称 : get_stations.py
# 创建时间 : 2019/6/7 20:48


import re
import requests
import os
import json

def get_station():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9101'
    response_get_station = requests.get(url,verify=True)
    # print(response)
    # print(response.text)
    stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)',response_get_station.text)
    print(stations)
    stations = dict(stations)
    stations = str(stations)
    # with open('stations.text','w+') as s:
    #     s.write(stations)
    write(stations,'stations.text')

def write(stations,file_name):
    with open(file_name, 'w',encoding='utf_8') as file:
        file.write(stations)
    # file = open(file_name,'w',enncoding='utf_8')
    # file.write(stations)
    # file.close()

def read(file_name):
    file = open(file_name,'r',encoding='utf_8')
    data = file.readline()
    file.close()
    return data

def is_stations(file_name):
    is_stations = os.path.exists(file_name)
    return is_stations

def get_selling_time():
    url = 'https://www.12306.cn/index/script/core/common/qss_v10029.js'
    response_selling_time = requests.get(url, verify=True)
    # str_response = str(response)
    with open('response.txt','w',encoding='utf_8') as file_respnose_selling_time:
        file_respnose_selling_time.write(response_selling_time.text)

    json_str = re.findall('{[^}]+}',response_selling_time.text)
    print(json_str)
    time_js = json.loads(json_str[0])
    write(str(time_js),'time.text')















