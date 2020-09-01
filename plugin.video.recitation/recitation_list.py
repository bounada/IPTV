import os

import json
import requests




path = os.path.dirname(__file__)
tags = []
recitation = []
ob1 = []
ob = []
for x in os.listdir(path + "/recitation_surat"):
    ob = {
            'name': x[:x.find('.')],
            'url': path + "/recitation_surat/" + x,
            'icon': '0.jpg'
        }
    recitation.append(ob)
    ob = []

ob = {
        'name': "Locale",
        'id': "Locale",
        'icon': '0.jpg'
    }
tags.append(ob)

j = 0
streams = {}
s = {
        "Locale" : recitation,
    }
streams.update(s)

try:
 res = requests.post("http://192.168.1.18:7000/recitation")
 data = res.text
 LiveTV = []
 tv = json.loads(data)

 recit = []
 for p in tv:

    ob = {
        'name': str(p),
        'id': str(p),
        'icon': str(p) +'.jpg'
    }
    tags.append(ob)
    ob = []

    for l in tv[p]:
        for i in l:
            recit.append(tv[p][l])

    s = {
        str(p): recit,
    }
    streams.update(s)
    recit = []

except:
  print("An exception occurred") 










