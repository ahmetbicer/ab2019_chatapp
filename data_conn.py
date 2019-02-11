import json
from urllib import request
url = "server_ip"

def send_message(isim, mesaj):
    data = json.dumps({"message":mesaj, "sender":isim}).encode()
    rq = request.Request(url, data, headers={'content-type': 'application/json'})
    response = request.urlopen(rq)
    return json.loads(response.read())

def get_message():
    return json.loads(request.urlopen(url).read())