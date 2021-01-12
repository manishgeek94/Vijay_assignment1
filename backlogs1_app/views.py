from django.shortcuts import render, HttpResponse
from .models import Student, Backlogs
from django.views.generic import View
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import StudentForm, BacklogsForm
import logging


# import logging
#
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')

@method_decorator(csrf_exempt, name='dispatch')
class Student_data(View):
    """This class basically helps to do all type of CRUD operation for Student Information in the database"""

    def get_student_by_id(self, id):
        try:
            student_info = Student.objects.get(student_id=id)
        except Student.DoesNotExist:
            student_info = None
        return student_info

    def get(self, request, *args, **kwargs):
        logging.basicConfig(filename='get_info.txt', level=logging.INFO)
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
                logging.info('student id not available in our system')
                return HttpResponse(json.dumps({'msg': 'student id not available in our system'},
                                               content_type='application/json'))
            logging.info('student id available in our system')
            return HttpResponse(b, content_type='application/json')

        qs = Student.objects.all()
        json_data = serialize('json', qs)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            stud_data = obj['fields']
            final_list.append(stud_data)
            json_data = json.dumps(final_list)
            logging.info(' %s Please find all student information', json_data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        logging.basicConfig(filename='create_info.txt', level=logging.INFO)
        data = request.body
        p_data = json.loads(data)
        form = StudentForm(p_data)
        if form.is_valid():
            obj = form.save(commit=True)
            logging.info(' %s Student added successfully', data)
            return HttpResponse(json.dumps({'msg': 'Student added successfully'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            logging.info("Something wrong with data")
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        logging.basicConfig(filename='update_info.txt', level=logging.INFO)
        data = request.body
        p_data = json.loads(data)
        student_id = p_data.get('id', None)
        if student_id is not None:
            stud_obj = self.get_student_by_id(student_id)
            if stud_obj is None:
                logging.info('Student id not available in our system')
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
                logging.info('Updated successfully')
                return HttpResponse(json.dumps({'msg': 'Updated successfully'}))
            if form.errors:
                json_data = json.dumps(form.errors)
                logging.info('Not Updated successfully')
                return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        logging.basicConfig(filename='delete_info.txt', level=logging.INFO)
        data = request.body
        print(data)
        p_data = json.loads(data)
        student_id = p_data.get('id', None)
        if student_id is not None:
            stud_obj = self.get_student_by_id(student_id)
            if stud_obj is None:
                logging.info('student_id data found to delete')
                return HttpResponse(json.dumps({'msg': 'Student id not available in our system'}),
                                    content_type='application/json')
            status, deleted_item = stud_obj.delete()
            if status == 1:
                logging.info('deleted successfully', deleted_item)
                return HttpResponse(json.dumps({'msg': 'deleted successfully'}))
            return HttpResponse(json.dumps({'msg': 'some issue occured ,try again'}))


@method_decorator(csrf_exempt, name='dispatch')
class Backlogs_data(View):
    """This class basically helps to do all type of CRUD operation for Backlogs Information in the database"""

    def get_backlogs_by_id(self, id):
        try:
            backlogs_info = Backlogs.objects.get(B_id=id)
            print(type(backlogs_info))
        except Backlogs.DoesNotExist:
            backlogs_info = None
        return backlogs_info

    def get(self, request, *args, **kwargs):
        logging.basicConfig(filename='get_backloginfo.txt', level=logging.INFO)
        data = request.body
        print(data)
        p_data = json.loads(data)
        backlogs_id = p_data.get('id', None)

        if backlogs_id is not None:
            backlogs_obj = self.get_backlogs_by_id(backlogs_id)
            if backlogs_obj is None:
                logging.info('backlog id not available in our system')
                return HttpResponse(json.dumps({'msg': 'id not available in our system'}
                                               ))
            else:
                a = {
                    'active_backlogs': backlogs_obj.active_backlogs,
                    'student_name': backlogs_obj.B_id.student_name,
                    'student_school': backlogs_obj.B_id.student_school,
                }
                b = json.dumps(a)
                logging.info(' %s student id available in our system', b)
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
        logging.basicConfig(filename='create_backloginfo.txt', level=logging.INFO)
        data = request.body
        p_data = json.loads(data)
        form = BacklogsForm(p_data)
        if form.is_valid():
            obj = form.save(commit=True)
            logging.info(" %s backlog info added", p_data)
            return HttpResponse(json.dumps({'msg': 'backlog added successfully'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            logging.info("backlog can't be added")
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        logging.basicConfig(filename='update_backloginfo.txt', level=logging.INFO)
        data = request.body
        print(data)
        p_data = json.loads(data)
        backlogs_id = p_data.get('id', None)
        if backlogs_id is not None:
            bcklgs_obj = self.get_backlogs_by_id(backlogs_id)
            if bcklgs_obj is None:
                logging.info('backlog id not available in our system')
                return HttpResponse(json.dumps({'msg': 'backlog id not available in our system'}),
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
                logging.info(' %s Updated successfully', old_backlogs)
                return HttpResponse(json.dumps({'msg': 'Updated successfully'}))
            if form.errors:
                json_data = json.dumps(form.errors)
                logging.error('Not Updated successfully')
                return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        logging.basicConfig(filename='delete_backloginfo.txt', level=logging.INFO)
        data = request.body
        print(data)
        p_data = json.loads(data)
        backlogs_id = p_data.get('id', None)
        if backlogs_id is not None:
            bcklgs_obj = self.get_backlogs_by_id(backlogs_id)
            if bcklgs_obj is None:
                logging.info('backlogid not found ')
                return HttpResponse(json.dumps({'msg': 'backlog id not available in our system'}),
                                    content_type='application/json')
            status, deleted_item = bcklgs_obj.delete()
            if status == 1:
                logging.info(' %s deleted successfully', deleted_item)
                return HttpResponse(json.dumps({'msg': 'deleted successfully'}))
            return HttpResponse(json.dumps({'msg': 'some issue occured ,try again'}))


@csrf_exempt
def atleast_one_record(request):
    """This function basically gives you name of student which is having atleast one active backlogs"""
    try:
        backlogs_obj = Backlogs.objects.filter(active_backlogs__gte=1)
    except Backlogs.DoesNotExist:
        backlogs_obj = None

    if backlogs_obj is None:
        return HttpResponse(json.dumps({'msg': 'No item found'}))
    else:
        empty_dict = {}
        for entry in backlogs_obj:
            empty_dict[entry.B_id.student_name] = entry.active_backlogs
        print(empty_dict)
        b = json.dumps(empty_dict)
        return HttpResponse(b, content_type='application/json')
