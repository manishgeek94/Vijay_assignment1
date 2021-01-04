import requests
import json


# def get_resource(id=None):
#     data = {
#
#     }
#     if data is not None:
#         data = {
#
#             'id': id
#         }
#
#     resp = requests.get('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
#
#
# get_resource(1002)

def create_resource():
    new_data = {

        'student_name': 'Manish',
        'student_id': 1005,
        'student_school': 'BSEB',
    }
    resp = requests.post('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())


create_resource()
#
# def update_resource(id):
#     data = {
#
#         'id': id,
#         'student_school': 'Holly cross',
#     }
#     resp = requests.put('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
#
#
# update_resource(1003)

# def delete_resource(id):
#     data = {
#
#         'id': id,
#
#     }
#     resp = requests.delete('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
#
#
# delete_resource(1002)
