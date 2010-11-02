#!/usr/bin/env python
# coding=utf-8

from time import sleep

from pysimplesoap.client import SoapClient, SoapFault

client = SoapClient(wsdl="http://localhost:8000/webservices/chatroom/call/soap?WSDL")

last_id = 0
while True:
    try:
        response = client.checkMessage(lastSeenId=last_id)
    except SoapFault:
        sleep(2)
    else:
        msg = response['Message']
        last_id = msg['id']
        print("{0} ({1}): {2}".format(msg['author'], msg['dateTime'], msg['text']))
