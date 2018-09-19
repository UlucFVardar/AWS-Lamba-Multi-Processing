# -*- coding: UTF-8 -*-

import requests
from layer_3_dataBase import DataBase as DB
from multiprocessing import Process
import boto3
import json
import time


def invoke_layer_4(payload):
    invokeLam = boto3.client("lambda", region_name = "eu-central-1")
    resp = invokeLam.invoke(FunctionName="layer_4", InvocationType="Event", Payload = json.dumps(payload))


def main(event, context):
    time_number = event['delay']
    try:
        url = 'https://api.ipify.org/?format=json'
        r = requests.get(url)

        ip = json.loads(r.text)['ip']
        layer = event['layer']
        number = event['number']
    except:
        ip = 'null'
        layer = event['layer']
        number = event['number']
    
    db = DB('innodb')
    db.insert(ip,layer,number)

    for i in range(1,21):
        
        payload = {"number": (number*10)+i, "layer": layer + 1, 'delay': time_number}
        # create and run process
        p = Process(target=invoke_layer_4, args=(payload,))
        p.start()        