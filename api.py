from flask import Flask, jsonify, request
from netmiko import Netmiko
from netmiko import ConnectHandler
from netmiko import file_transfer
import json

app = Flask(__name__)

# linux = {
#     "device_type": 'linux',
#     "ip":'10.33.109.109',
#     "username": 'ubuntu',
#     "password": 'ubuntu1234',
#     "port":22,
#     "verbose":True,
#     "secret":"ubuntu1234"
# }

# connection = ConnectHandler(**linux)
# connection.enable()
# buatfolder = onnection.send_command('ls')

database = []
with open("dataeng.json",'r') as db:
    data = json.load(db)
for x in data:
    database.append(x)
db.close()

@app.route("/")
def hello():
    return "Assalamu'alaikum Ukhtyyy.."

@app.route("/database/test", methods=["GET"])
def getAll():
    return jsonify({'test':database})

@app.route("/database/test/<testId>", methods=['GET'])
def getTest(testId):
    usr = [test for test in database if (test["label"] == testId)]
    return jsonify({'test':usr})

if __name__=="__main__":
    app.run()