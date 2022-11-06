
from flask import Flask, render_template, make_response, Response
from flask_restful import Api, Resource


def mac_standardize(mac_address, standard=":", character="lower"):
    import re
    '''
        Formar wejściowy i wyjściowy MAC adresu:
            MM:MM:MM:SS:SS:SS
            MM-MM-MM-SS-SS-SS
            MMM.MMM.SSS.SSS
    '''
    # Czyścimy i ujednolicamy format MAC adresu.
    mac_address = str(mac_address).strip(' :.-')
    mac_address = re.sub(r'[^a-fA-F0-9]', '', mac_address)
    # Dostosowujemy wielkość znaków w MAC adresie.
    if character == "lower":
        mac_address = mac_address.lower()
    elif character == "upper":
        mac_address = mac_address.upper()

    if standard == ":":
        mac_address == mac_address[0-2] + ":" + mac_address[2-4] + ":" + mac_address[4-6] + ":" + mac_address[6-8] + ":" + mac_address[8-10] + ":" + mac_address[10-12]
    elif standard == "-":
        mac_address == mac_address[0-2] + "-" + mac_address[2-4] + "-" + mac_address[4-6] + "-" + mac_address[6-8] + "-" + mac_address[8-10] + "-" + mac_address[10-12]
    elif standard == ".":
        mac_address == mac_address[0-3] + "." + mac_address[3-6] + "." + mac_address[6-9] + "." + mac_address[9-12]
    return mac_address


def login_to_evio_stb(mac):
    user = mac_standardize(mac, standard="", character="upper")
    passwd = user[::-1]
    return (user, passwd)


class EvioLogin(Resource):
    def get(self, mac_address="", ip="127.0.0.1"):
        data=dict()
        data['user'], data['passwd'] = login_to_evio_stb(mac_address)
        data['ip'] = ip
        return Response(response=render_template('evio.html',d=data))

class Status(Resource):
    def get(self):
        return "Status OK"

    def post(self):
        return "Status OK"

    def put(self):
        return "Status OK"

    def delete(self):
        return "Status OK"

def create_app():
    app=Flask(__name__)

    # Flask RESTful
    api = Api(app)
    api.add_resource(Status, '/')
    api.add_resource(EvioLogin, '/Evio/<ip>/<mac_address>/login')

    return app