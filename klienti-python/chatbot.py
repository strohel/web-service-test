#!/usr/bin/env python
# coding=utf-8

from pysimplesoap.client import SoapClient, SoapFault

client = SoapClient(wsdl="http://localhost:8000/webservices/chatroom/call/soap?WSDL")

client.sendMessage(author="Robot 1", text="Lorem ipsum dolor sit amet")
client.sendMessage(author="Robot 2", text="Heej, ja chci taky neco rict!")
client.sendMessage(author="Robot 1", text="No tak to rekni!")
