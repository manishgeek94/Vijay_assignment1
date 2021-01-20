import json
import requests


def test_get_resource(id=10096):
    data = {

    }
    if data is not None:
        data = {

            'id': id
        }

    resp = requests.get('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200


def test_get_unknown_resource(id=10020):
    data = {

    }
    if data is not None:
        data = {

            'id': id
        }

    resp = requests.get('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200



