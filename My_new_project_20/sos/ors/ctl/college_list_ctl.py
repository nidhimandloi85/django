from django.shortcuts import render

from .base_ctl import BaseCtl
from ..service.college_service import CollegeService


class CollegeListCtl(BaseCtl):

    def request_to_form(self,request):
       self.form['name'] = request.POST.get('Name')

    def display(self,request,params ={}) :
        college_list = self.get_service().search(self.form)
        self.form['list'] = college_list
        return render(request, self.get_template(), {"form": self.form})

    def submit(self,request,param={}):
        if request.POST['operation'] == "next":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] += 1

        if request.POST['operation'] == "previous":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] -= 1

        if request.POST['operation'] == "search":
            self.form['page_no'] = 1
            self.request_to_form(request)

        college_list = self.get_service().search(self.form)
        self.form['list'] = college_list
        return render(request, self.get_template(), {"form": self.form})

    def get_template(self ):
        return 'college_list.html'
    def get_service(self):
        return CollegeService()
