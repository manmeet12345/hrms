from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name = "homepage"),
    path("login/",views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path("logout/",views.logoutUser,name="logout"),
    path("time_management/",views.time_management,name="time_management"),
    path('employee_manage/',views.employee_manage,name='employee_manage'),
    path('add_employee/',views.add_employee,name='add_employee'),
    path('employee_details/',views.employee_details,name='employee_details'),
    path('update_employee/<str:pk>',views.update_employee,name='update_employee'),
    path('delete_employee/<int:pk>',views.delete_employee,name='delete_employee')
]
