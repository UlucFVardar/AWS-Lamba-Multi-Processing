# -*- coding: UTF-8 -*-

import requests
from layer_3_dataBase import DataBase as DB
from multiprocessing import Process
import boto3
import json
import time

def main(event, context):

    time.sleep(event['delay'])
    
    url = 'https://api.ipify.org/?format=json'
    r = requests.get(url)

    ip = json.loads(r.text)['ip']
    layer = event['layer']
    number = event['number']

    db = DB('innodb')
    db.insert(ip,layer,number)