from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import Student
from ..service.college_service import CollegeService
from ..service.student_service import StudentService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility


class StudentCtl(BaseCtl):

    def preload(self, request):
        college_list = CollegeService().search({})

        self.form['preload_list'] = college_list
        self.preload_data['college_select'] = HtmlUtility.get_list_from_beans(
            "collegeId",
            self.form.get("college_id"),
            college_list
        )
        return self.preload_data

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if (DataValidator.is_null(request.POST.get("firstName", ''))):
            input_error['first_name'] = ' Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("lastName", ''))):
            input_error['last_name'] = 'last Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("dob", ''))):
            input_error['dob'] = ' Dob is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("mobile_number", ''))):
            input_error['mobile_number'] = ' Mobile_number is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("email", ''))):
            input_error['email'] = 'email is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['college_id']) or request.POST.get("collegeId") == "0"):
            input_error['college_id'] = 'College is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['first_name'] = request.POST.get('firstName')
        self.form['last_name'] = request.POST.get('lastName')
        self.form['dob'] = request.POST.get('dob')
        self.form['mobile_number'] = request.POST.get('mobile_number')
        self.form['email'] = request.POST.get('email')
        self.form['college_id'] = int(request.POST.get('collegeId', 0))

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.first_name = self.form['first_name']
        obj.last_name = self.form['last_name']
        obj.dob = self.form['dob']
        obj.mobile_number = self.form['mobile_number']
        obj.email = self.form['email']
        obj.college_id = int(self.form['college_id'])
        obj.college_name = CollegeService().get(self.form['college_id']).name
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['first_name'] = obj.first_name
        self.form['last_name'] = obj.last_name
        self.form['dob'] = obj.dob
        self.form['mobile_number'] = obj.mobile_number
        self.form['email'] = obj.email
        self.form['college_id'] = obj.college_id
        self.form['college_name'] = obj.college_name

    def display(self, request, params={}):

        return render(request, self.get_template(), {'form': self.form, "preload_data": self.preload(request)})

    def submit(self, request, params={}):
        try:
            student = self.form_to_model(Student())
            self.get_service().save(student)
            if self.form['id'] > 0:
                self.form['message'] = 'Student Updated Successfully...!!!'
            else:
                self.form['message'] = 'Student Added Successfully...!!!'
        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True
        return render(request, self.get_template(), {'form': self.form, "preload_data": self.preload(request)})

    def get_service(self):
        return StudentService()

    def get_template(self):
        return 'Student.html'
