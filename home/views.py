from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import employee, Timetrack
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
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
    if request.user.is_authenticated:

        return render(request,"time_management.html")
    else:
        return redirect('/home/login/')


def employee_manage(request):
    if request.user.is_authenticated:
        return render(request,'employee_manage.html')
    else:
        return redirect('/home/login/')

def add_employee(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        department = request.POST.get('department')
        birth_date = request.POST.get('birth_date')
        designation = request.POST.get('designation')
        emp_code = request.POST.get('emp_code')
        
        employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            address=address,
            department=department,
            birth_date=birth_date,
            title=designation,
            emp_code = emp_code
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
        emp_code = request.POST.get('emp_code')
        
        emp.first_name = first_name
        emp.last_name = last_name
        emp.phone_no = phone_no
        emp.address = address
        emp.department = department
        emp.birth_date = birth_date
        emp.title = designation
        emp.emp_code = emp_code
        
        emp.save()
        return redirect('employee_details')
    return render(request,'update_employee.html',{'emp':emp})

def delete_employee(request,pk):
    emp = employee.objects.get(id=pk)
    emp.delete()
    return redirect('employee_details')

def time_track(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        description = request.POST.get('description')
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')

        start_time = None
        end_time = None

        # Convert string values to datetime objects
        if start_time_str:
            start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')

        if end_time_str:
            end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')

        Timetrack.objects.create(
            employee = username,
            description = description,
            start_time = start_time,
            end_time = end_time

        )
        return render(request,'time_track.html')
    return render(request, 'time_track.html')

def view_timetrack(request):
    timetracks = Timetrack.objects.all()
    

    return render(request,'view_timetrack.html',{'timetracks':timetracks})

'''def chatbot_view(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(settings.DIALOGFLOW_PROJECT_ID, request.session.session_id)

        text_input = dialogflow.TextInput(text=query, language_code='en')
        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        response_text = response.query_result.fulfillment_text
        context = {'response': response_text}
        return render(request, 'chatbot.html', context)

    return render(request, 'chatbot.html')'''