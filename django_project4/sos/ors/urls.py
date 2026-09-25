from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',views.user_signin),
    path('signup/',views.user_signup),
    path('welcome/',views.welcome),
    path('logout/',views.user_logout),
    path('list/', views.user_list),
    path('delete/<int:id>/',views.delete_user),
    path('save/',views.user_save),
    path('save/<int:id>/',views.user_save),


    path('',views.welcome),
]