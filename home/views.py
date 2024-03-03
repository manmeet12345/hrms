from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import employee
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
# Create your views here.

def homepage(request):
    
    return render(request,"landing_page.html")

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'Username is not registered.')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request,'Username or password does not exist')
    context = {}
    return render(request,'login_register.html',context)

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request,"An error occured during the registration")
    return render(request,'register.html',{'form':form})

def logoutUser(request):
    logout(request)
    return redirect('homepage')

def time_management(request):
    return render(request,"time_management.html")

def employee_manage(request):
    return render(request,'employee_manage.html')

def add_employee(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        department = request.POST.get('department')
        birth_date = request.POST.get('birth_date')
        designation = request.POST.get('designation')
        
        employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            address=address,
            department=department,
            birth_date=birth_date,
            title=designation
        )
        return render(request,'add_employee.html')
        
    return render(request,'add_employee.html')

def employee_details(request):
    employees = employee.objects.all()
    '''query = request.GET.get('q')
    if query:
        employee_list = employees.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(phone_no__icontains=query) |
            Q(address__icontains=query) |
            Q(department__icontains=query) |
            Q(title__icontains=query)
        )

    # Pagination
    paginator = Paginator(employees, 10)  # Show 10 employees per page
    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)'''

    return render(request,'employee_details.html',{'employees':employees})

def update_employee(request,pk):
    emp = employee.objects.get(id=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        department = request.POST.get('department')
        birth_date = request.POST.get('birth_date')
        designation = request.POST.get('designation')
        
        emp.first_name = first_name
        emp.last_name = last_name
        emp.phone_no = phone_no
        emp.address = address
        emp.department = department
        emp.birth_date = birth_date
        emp.title = designation
        
        emp.save()
        return redirect('employee_details')
    return render(request,'update_employee.html',{'emp':emp})

def delete_employee(request,pk):
    emp = employee.objects.get(id=pk)
    emp.delete()
    return redirect('employee_details')