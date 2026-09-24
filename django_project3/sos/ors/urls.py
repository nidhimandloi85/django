from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/',views.display),
    path('signin/',views.user_signin),
    path('signup/',views.user_signup),
    path('welcome/',views.welcome),
    path('testlist/',views.test_list),
    path('logout/',views.user_logout),
    path('list/', views.user_list),
    path('delete/<int:id>/',views.delete_user),
    path('edit/<int:id>/',views.edit_user),
    path('save/',views.user_save),
    path('create/', views.create_session),
    path('access/', views.access_session),
    path('destroy/', views.destroy_session),
    path('set/', views.setCookies),
    path('get/', views.getCookies),


    path('',views.welcome),
]