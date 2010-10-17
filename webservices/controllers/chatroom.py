# coding: utf8
"""
Jednoducha chatovaci sluzba. Od klientu se ceka, ze budou volat
checkMessage() kazdych par (2) sekund. Jako parametr se preda id posledni zpravy,
kterou klient od serveru dostal nebo 0, pokud jeste zadnou nedostal.

checkMessage() bud vrati zpravu nebo Fault, coz znamena, ze v danou chvili neni
dostupna zadna novejsi zprava. Na toto klient nemusi a nemel by nijak reagovat.
Pokud checkMessage() vrati zpravu, tak klient muze a mel by znovu zavolat
checkMessage() a tak pokacovat az do doby, kdy uz zadne nove zpravy nebudou.

Pokud chce klient poslat zpravu, zavola sendMessage(). Vrati se true nebo false
podle toho, zda server zpravu prijme.

Od klientu se ceka, ze i vlastni zpravy zobrazi az kdyz je zpet ziskaji
pomoci checkMessage(), nikoliv jiz pri odeslani.
"""

from datetime import datetime

from gluon.tools import Service

service = Service(globals())

def get_cache():
    if 'messages' not in cache.ram.storage:
        cache.ram.storage['messages'] = []
    if 'last_msg_id' not in cache.ram.storage:
        cache.ram.storage['last_msg_id'] = 0
    return cache.ram.storage

def get_messages():
    return get_cache()['messages']



class Message(object):

    def __init__(self, author, text):
        cache = get_cache()
        cache['last_msg_id'] += 1
        self.id = cache['last_msg_id']
        self.dateTime = datetime.today().replace(microsecond=0)  # microseconds may confuse some clients
        if not isinstance(author, str):
            raise AttributeError("author attribute must be (a subtype of) string")
        self.author = author
        if not isinstance(text, str):
            raise AttributeError("text attribute must be (a subtype of) string")
        self.text = text

    def to_dict(self):
        return {'id':self.id,
                'dateTime':self.dateTime,
                'author':self.author,
                'text':self.text}




@service.soap('sendMessage',
    returns={'messageId':int},
    args={'author':str, 'text':str})
def sendMessage(author, text):
    """Posle zpravu do chatroomu"""
    messages = get_messages()
    msg = Message(author, text)
    messages.append(msg)
    if len(messages) > 20:  # limitujeme pocet zapamatovanych zprav
        del messages[0]
    return msg.id


@service.soap('checkMessage',
    returns={'Message':{'id':int, 'dateTime':datetime, 'author':str, 'text':str}},
    args={'lastSeenId':int})
def checkMessage(lastSeenId):
    """Zjisti, zda je na serveru novejsi zprava nez ta s id lastSeenId a vrati ji"""
    messages = get_messages()

    # najdeme prvni zpravu, ktera ma vetsi id (nepocitame s pretecenim)
    for msg in messages:
        if msg.id > lastSeenId:
            return msg.to_dict()
    raise LookupError("no newer messages")



def call():
    response.title = "ChatRoom"  # toto je binding a service name v WSDL
    response.description = __doc__  # toto prida dokumentaci do WSDL atd.
    return service()
