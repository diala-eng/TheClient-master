from flask import Flask, jsonify
import requests
app = Flask(__name__)

i = int(input("enter your option from 1-3 ,1: search id. 2: search topic. 3:ppurchase. : "))

def search(i):
        option = input("enter topic or id")
        switcher={
                 "1": # option = int(input("enter id"))
                    searchID(int(option)),
                "2":# option = input("enter topic")
                    searchTopic(option),
                "3": # option = int(input("enter id"))
                    purchase(int(option))
                }
        return switcher.get(i,"Invalid")


def searchID(id):
    req=requests.get("http://192.168.100.8:7000/searchID/{}".format(id))

    if req.status_code == 200:
        result=req.json() #content of json as dictionary
        return jsonify(result)
    elif req.status_code == 404:
        return 'The server has not found anything matching the URI given'
    else:
        return 'Status code '+ req.status_code +' indicates to something ERROR!'



def searchTopic(topic):
    req=requests.get("http://192.168.100.8:7000/searchTopic/{}".format(topic)) #send to catalog

    if req.status_code == 200:
        result=req.json() #content of json as dictionary
        return jsonify(result)
    elif req.status_code == 404:
        return 'The server has not found anything matching the URI given'
    else:
        return 'Status code '+ req.status_code +' indicates to something ERROR!'

def purchase(id):

    req = requests.get("http://192.168.100.9:9000/purchase/{}".format(id))
    if req.status_code == 200:
        result = req.json()  # content of json as dictionary
        print('beautiful')
        return jsonify(result)
    elif req.status_code == 404:
        return 'The server has not found anything matching the URI given'
    else:
        return 'Status code indicates to something ERROR!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)