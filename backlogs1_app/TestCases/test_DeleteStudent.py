import json
import requests


def test_delete_student(id=10096):
    data = {

                'id': id,
            }
    resp = requests.put('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200


def test_delete_unknown_id(id=100100):
    data = {

        'id': id,
    }
    resp = requests.put('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200
