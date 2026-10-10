from django.shortcuts import render,redirect
from .base_ctl import BaseCtl
from ..service.role_service import RoleService
from ..service.user_service import UserService


class RoleListCtl(BaseCtl):

    def request_to_form(self,request):
       self.form['name'] = request.POST.get('name')

    def display(self,request,params={}):
        role_list = self.get_service().search(self.form)
        self.form['list'] = role_list
        return render(request, self.get_template(), {"form": self.form})

    def submit(self,request,params={}):
        if request.POST['operation'] == "next":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] += 1

        if request.POST['operation'] == "previous":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] -= 1

        if request.POST['operation'] == "search":
            self.form['page_no'] = 1
            self.request_to_form(request)

        role_list= self.get_service().search(self.form)
        self.form['list'] = role_list
        return render(request, self.get_template(), {"form": self.form})

    def get_template(self):
        return "role_list.html"
    def get_service(self):
        return RoleService()


