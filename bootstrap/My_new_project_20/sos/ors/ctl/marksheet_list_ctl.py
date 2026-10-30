from django.shortcuts import render

from .base_ctl import BaseCtl
from ..service.marksheet_service import MarksheetService


class MarksheetListCtl(BaseCtl):

    def request_to_form(self,request):
       self.form['roll_number'] = request.POST.get('roll_number')

    def display(self,request,params ={}) :
        marksheet_list = self.get_service().search(self.form)
        self.form['list'] = marksheet_list
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

        marksheet_list = self.get_service().search(self.form)
        self.form['list'] = marksheet_list
        return render(request, self.get_template(), {"form": self.form})

    def get_template(self ):
        return 'marksheet_list.html'
    def get_service(self):
        return MarksheetService()
