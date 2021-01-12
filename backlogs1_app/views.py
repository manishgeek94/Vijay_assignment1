from django.shortcuts import render, HttpResponse
from .models import Student, Backlogs
from django.views.generic import View
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import StudentForm,BacklogsForm
import logging



@method_decorator(csrf_exempt, name='dispatch')
class Student_data(View):
    def get_student_by_id(self, id):
        try:
            student_info = Student.objects.get(student_id=id)
        except Student.DoesNotExist:
            student_info = None
        return student_info

    def get(self, request, *args, **kwargs):
        logging.basicConfig(filename='get_info.txt')
        data = request.body
        print(data)
        p_data = json.loads(data)
        student_id = p_data.get('id', None)

        if student_id is not None:
                stud_obj = self.get_student_by_id(student_id)

                a = {
                    'name': stud_obj.student_name,
                    'school': stud_obj.student_school
                }

                b = json.dumps(a)

                if stud_obj is None:
                    logging.error('student id not available in our system')
                    return HttpResponse(json.dumps({'msg': 'student id not available in our system'},
                                                   content_type='application/json'))
                logging.error('student id available in our system')
                return HttpResponse(b, content_type='application/json')

        qs = Student.objects.all()
        json_data = serialize('json', qs)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            stud_data = obj['fields']
            final_list.append(stud_data)
            json_data = json.dumps(final_list)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        logging.basicConfig(filename='create_info.txt')
        data = request.body
        p_data = json.loads(data)
        form = StudentForm(p_data)
        if form.is_valid():
            obj = form.save(commit=True)
            logging.info('Student added successfully')
            return HttpResponse(json.dumps({'msg': 'Student added successfully'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            logging.error("Student can't be added")
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        logging.basicConfig(filename='update_info.txt')
        data = request.body
        p_data = json.loads(data)
        student_id = p_data.get('id', None)
        if student_id is not None:
            stud_obj = self.get_student_by_id(student_id)
            if stud_obj is None:
                logging.error('Student id not available in our system')
                return HttpResponse(json.dumps({'msg': 'Student id not available in our system'}),
                                    content_type='application/json')
            new_student = p_data

            old_student = {
                'student_name': stud_obj.student_name,
                'student_id': stud_obj.student_id,
                'student_school': stud_obj.student_school,

            }

            old_student.update(new_student)
            form = StudentForm(old_student, instance=stud_obj)
            if form.is_valid():
                form.save(commit=True)
                logging.error('Updated successfully')
                return HttpResponse(json.dumps({'msg': 'Updated successfully'}))
            if form.errors:
                json_data = json.dumps(form.errors)
                logging.error('Not Updated successfully')
                return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        logging.basicConfig(filename='delete_info.txt')
        data = request.body
        print(data)
        p_data = json.loads(data)
        student_id = p_data.get('id', None)
        if student_id is not None:
            stud_obj = self.get_student_by_id(student_id)
            if stud_obj is None:
                logging.error('not found successfully')
                return HttpResponse(json.dumps({'msg': 'Student id not available in our system'}),
                                    content_type='application/json')
            status, deleted_item = stud_obj.delete()
            if status == 1:
                logging.error('deleted successfully', deleted_item)
                return HttpResponse(json.dumps({'msg': 'deleted successfully'}))
            return HttpResponse(json.dumps({'msg': 'some issue occured ,try again'}))


@method_decorator(csrf_exempt, name='dispatch')
class Backlogs_data(View):
    def get_backlogs_by_id(self, id):
        try:
            backlogs_info = Backlogs.objects.get(B_id=id)
        except Backlogs.DoesNotExist:
            backlogs_info = None
        return backlogs_info

    def get(self, request, *args, **kwargs):
        # logging.basicConfig(filename='get_info.txt')
        data = request.body
        print(data)
        p_data = json.loads(data)
        backlogs_id = p_data.get('id', None)

        if backlogs_id is not None:
            backlogs_obj = self.get_backlogs_by_id(backlogs_id)
            if backlogs_obj is None:
                # logging.error(' id not available in our system')
                return HttpResponse(json.dumps({'msg': 'id not available in our system'}
                                               ))
            # logging.error('student id available in our system')
            else:
                a = {
                    'active_backlogs': backlogs_obj.active_backlogs,
                    'student_name': backlogs_obj.B_id.student_name,
                    'student_school': backlogs_obj.B_id.student_school,
                }
                b = json.dumps(a)
                return HttpResponse(b, content_type='application/json')

        qs = Backlogs.objects.all()
        json_data = serialize('json', qs)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            stud_data = obj['fields']
            final_list.append(stud_data)
        json_data = json.dumps(final_list)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        logging.basicConfig(filename='create_info.txt')
        data = request.body
        p_data = json.loads(data)
        form = BacklogsForm(p_data)
        if form.is_valid():
            obj = form.save(commit=True)
            return HttpResponse(json.dumps({'msg': 'backlog added successfully'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            logging.error("backlog can't be added")
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        logging.basicConfig(filename='update_info.txt')
        data = request.body
        print(data)
        p_data = json.loads(data)
        backlogs_id = p_data.get('id', None)
        if backlogs_id is not None:
            bcklgs_obj = self.get_backlogs_by_id(backlogs_id)
            if bcklgs_obj is None:
                logging.error('Student id not available in our system')
                return HttpResponse(json.dumps({'msg': 'Student id not available in our system'}),
                                    content_type='application/json')
            new_backlogs = p_data

            old_backlogs = {
                'B_id': bcklgs_obj.B_id,
                'active_backlogs': bcklgs_obj.active_backlogs
            }

            old_backlogs.update(new_backlogs)
            form = BacklogsForm(old_backlogs, instance=bcklgs_obj)
            if form.is_valid():
                form.save(commit=True)
                # logging.error('Updated successfully')
                return HttpResponse(json.dumps({'msg': 'Updated successfully'}))
            if form.errors:
                json_data = json.dumps(form.errors)
                logging.error('Not Updated successfully')
                return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        logging.basicConfig(filename='delete_info.txt')
        data = request.body
        print(data)
        p_data = json.loads(data)
        backlogs_id = p_data.get('id', None)
        if backlogs_id is not None:
            bcklgs_obj = self.get_backlogs_by_id(backlogs_id)
            if bcklgs_obj is None:
                logging.error('not found successfully')
                return HttpResponse(json.dumps({'msg': 'Student id not available in our system'}),
                                    content_type='application/json')
            status, deleted_item = bcklgs_obj.delete()
            if status == 1:
                logging.error('deleted successfully')
                return HttpResponse(json.dumps({'msg': 'deleted successfully'}))
            return HttpResponse(json.dumps({'msg': 'some issue occured ,try again'}))

@csrf_exempt
def atleast_one_record(request):
    backlogs_obj = Backlogs.objects.filter(active_backlogs__gte=12)
    json_data = serialize('json', backlogs_obj)
    print(backlogs_obj)
    p_data = json.loads(json_data)
    final_list = []
    for obj in p_data:
        stud_data = obj['fields']
        final_list.append(stud_data)
    json_data = json.dumps(final_list)
    return HttpResponse(json_data, content_type='application/json')






