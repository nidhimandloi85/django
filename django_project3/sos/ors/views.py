from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .service.user_service import UserService


# Create your views here.
def display(request):
    return HttpResponse('<h3> hlo display </h3>')

def welcome(request):
    return render(request,'welcome.html')

def user_signin(request):
    message=''
    if request.method=='POST':
        form={}
        form['login_id']=request.POST.get('loginId')
        form['password']=request.POST.get('password')

        service=UserService()
        records=service.authenticate(form['login_id'],form['password'])

        if len(records)>0:
            request.session['first_name']=records[0].get('first_name')
            return redirect('/ors/welcome/')
        else:
            message='loginId & password invalid'
    return render(request,'login.html',{'message':message})

def user_signup(request):
    if request.method=='POST':
        form={}
        form['first_name']=request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        service=UserService()
        service.add(form)
    return render(request,'registration.html')

def test_list(request):
    list=[
        {"id": 1, "first_name": "Rahul", "last_name": "Sharma", "email": "rahul@gmail.com", "password": "rahul123"},
        {"id": 2, "first_name": "nidhi", "last_name": "mandloi", "email": "nidhi@gmail.com", "password": "nidhi123"},
        {"id": 3, "first_name": "harshad", "last_name": "niboriya", "email": "harshad@gmail.com", "password": "harshad123"},
        {"id": 4, "first_name": "vikash", "last_name": "varma", "email": "rahul@gmail.com", "password": "rahul123"},
        {"id": 5, "first_name": "harshit", "last_name": "choudhary", "email": "harshit@gmail.com", "password": "harshit123"},
    ]
    return render(request,'test_list.html',{'list':list})

def user_logout(request):
    request.session['first_name']= None
    return redirect('/ors/signin/')


def delete_user(request, id=0):
    service = UserService()
    service.delete(id)
    return redirect("/ors/list/")

def user_list(request):
    form={}
    form['page_no']= 1
    form['page_size']= 5
    if request.method == "POST":

         if request.POST['operation']=='next':
              form['page_no']=int(request.POST.get('pageNo'))
              form['page_no'] += 1
         if request.POST['operation'] == 'previous':
             form['page_no']=int(request.POST.get('pageNo'))
             form['page_no'] -=1
         if request.POST['operation'] == "search":
             form['page_no'] = 1
             form['first_name'] = request.POST.get('firstName')

    service=UserService()
    list=service.search(form)
    index=(form['page_no'] - 1 )* form['page_size']
    return render(request,'user_list.html',{'list':list,'page_no':form['page_no'],'index':index})

def edit_user(request,id=0):
    service = UserService()
    user_data = service.get(id)
    return render(request,'user.html',{'data': user_data[0]})

def user_save(request):
    if request.method=='POST':
        form={}
        form['id']=request.POST.get('id',0)
        form['first_name']=request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        service=UserService()
        if form['id'] != '' and int(form['id'])> 0:
            service.update(form)
        else:
            service.add(form)
    return render(request,'user.html')


def create_session(request):
    request.session['name'] = 'Admin'
    response = "<h1>Welcome To Sessions</h1><br>"
    response += "ID : {0} <br>".format(request.session.session_key)
    return HttpResponse(response)

def access_session(request):
    response = "Name : {0} <br>".format(request.session.get('name'))
    return HttpResponse(response)

def destroy_session(request):
    Session.objects.all().delete()
    return HttpResponse("Session is Destroy")

def setCookies(request):
    key = "name"
    value = "abc"
    res = HttpResponse("<h1>cookie created..!!</h1>")
    res.set_cookie(key, value, max_age=60)
    return res

def getCookies(request):
    value = request.COOKIES.get('name')
    html = "<h3><center> value = {} </center></h3>".format(value)
    return HttpResponse(html)


