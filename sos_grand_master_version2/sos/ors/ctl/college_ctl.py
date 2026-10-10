from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import College
from ..service.college_service import CollegeService
from ..utility.data_validator import DataValidator


class CollegeCtl(BaseCtl):

    def input_validation(self, request):
        operation = request.POST.get('operation', '')
        if operation == 'reset':
            return False
        input_error = self.form.get("input_error")
        input_error['error'] = False
        if (DataValidator.is_null(request.POST.get("name", ''))):
            input_error['name'] = 'Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("address", ''))):
            input_error['address'] = 'address is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("state", ''))):
            input_error['state'] = 'state is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("city", ''))):
            input_error['city'] = 'city is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("phone_number", ''))):
            input_error['phone_number'] = 'phone_number is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['name'] = request.POST.get('name')
        self.form['address'] = request.POST.get('address')
        self.form['state'] = request.POST.get('state')
        self.form['city'] = request.POST.get('city')
        self.form['phone_number'] = request.POST.get('phone_number')

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.name = self.form['name']
        obj.address = self.form['address']
        obj.state = self.form['state']
        obj.city = self.form['city']
        obj.phone_number = self.form['phone_number']
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['address'] = obj.address
        self.form['state'] = obj.state
        self.form['city'] = obj.city
        self.form['phone_number'] = obj.phone_number



    def display(self, request, params = {}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request,params = {}):
            try:
                college = self.form_to_model(College())
                self.get_service().save(college)

                if self.form['id'] > 0:
                    self.form['message'] = 'College Updated Successfully...!!!'
                else:

                    self.form['message'] = 'College Added Successfully...!!!'

            except Exception as e:
                self.form['message'] = str(e)
                self.form['error'] = True

            return render(request,self.get_template(), {'form': self.form})

    def get_service(self):
        return CollegeService()

    def get_template(self):
        return 'college.html'