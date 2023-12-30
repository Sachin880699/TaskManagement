from django.shortcuts import render, redirect
from accounts.models import *
from django.db.models import Q
from django.contrib import auth
from datetime import date
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def task(request):
    current_user = request.user
    all_member      = EmployeeUser.objects.all()
    task_obj        = EmployeeTask.objects.filter(created_at = date.today())
    if request.method == 'POST':
        filter_date            = request.POST.get("filter_date")
        filter_by         = request.POST.get("filter_by")
        member      = EmployeeUser.objects.get(id = filter_by)
        task_obj         = EmployeeTask.objects.filter(member = member,created_at = filter_date)

    context = {
        'task_obj':task_obj,
        'all_member':all_member,
        'current_member_id':current_user.id
    }
    return render(request,'task.html',context)

@login_required(login_url='login')
def task_details(request,id):
    task_obj         = EmployeeTask.objects.get(id = id)
    estimate_time    = task_obj.estimated_time.split(":")
    actual_time      = task_obj.actual_time.split(":")
    context = {
        'task_obj':task_obj,
        'estimate_time':estimate_time,
        'actual_time':actual_time
    }
    return render(request,'task_details.html',context)

@login_required(login_url='login')
def update_task(request,id):
    task_obj        = EmployeeTask.objects.get(id = id)
    all_task_status = TaskStatus.objects.all()
    all_project     = Project.objects.all()
    if request.method == 'POST':
        assign_project       = request.POST.get("assign_project")
        task                 = request.POST.get("task")
        task_status                 = request.POST.get("task_status")
        task_date            = request.POST.get("task_date")
        task_hours          =  request.POST.get("task_hours")
        task_minutes        =  request.POST.get("task_minutes")
        actual_time_task_hours    = request.POST.get("actual_time_task_hours")
        actual_time_task_minutes  = request.POST.get("actual_time_task_minutes")

        project_obj             = Project.objects.get(id = assign_project)
        task_status             = TaskStatus.objects.get(id = task_status)

        emp_task_obj            = EmployeeTask.objects.create(
            description         = task,
            created_at          = task_date,
            task_status         = task_status,
            project             = project_obj,
            estimated_time      = f"{task_hours}:{task_minutes}",
            actual_time         = f"{actual_time_task_hours}:{actual_time_task_minutes}",
            member              = request.user
        )
        return redirect("task")

    context = {
        'task_obj':task_obj,
        'all_task_status':all_task_status,
        'all_project':all_project
    }
    return render(request,'update_task.html',context)

@login_required(login_url='login')
def create_task(request):
    current_user = request.user
    employee_assing_project  = Project.objects.filter(assign_to = current_user)
    if request.method == 'POST':
        assign_project               =  request.POST.get('assign_project')
        task                         =  request.POST.get('task')
        task_hours                   =  request.POST.get('task_hours')
        task_minutes                 =  request.POST.get('task_minutes')

        task_status_obj              = TaskStatus.objects.get(task_status = 'To-Do')

        project                      = Project.objects.get(id = assign_project)
        create_task_obj              = EmployeeTask.objects.create(
            description                = task,
            project             = project,
            member              = current_user,
            estimated_time      = f"{task_hours}:{task_minutes}",
            task_status         = task_status_obj
        )
        return redirect("/")


    context = {
        'employee_assing_project':employee_assing_project,
    }
    return render(request,'create_task.html',context)


@login_required(login_url='login')
def member(request):
    all_member = EmployeeUser.objects.all()
    context = {
        'all_member':all_member
    }
    return render(request,'member.html',context)

@login_required(login_url='login')
def add_member(request):

    member_status       =   EmployeeStatus.objects.all()
    member_role         =   EmployeeRole.objects.all()
    report_to_employee  =   EmployeeUser.objects.all()
    experty             =   Experty.objects.all()

    if request.method == 'POST':
        name                    =       request.POST.get("employee_name")
        email                   =       request.POST.get("email")
        member_status_id        =       request.POST.get("employee_status")
        employee_role           =       request.POST.get("employee_role")
        password                =       request.POST.get("password")
        report_to               =       request.POST.get("report_to")
        expert_list             =       request.POST.getlist('experty[]')

        member_status_obj       =       EmployeeStatus.objects.get(id = member_status_id)
        employee_role_obj       =       EmployeeRole.objects.get(id = employee_role)
        report_to_obj           =       EmployeeUser.objects.get(id = report_to)

        new_employee_obj        =       EmployeeUser.objects.create_user(
            email            =  email,
            password        =  password )

        new_employee_obj        =       EmployeeUser.objects.get(id = new_employee_obj.id)
        new_employee_obj.name           = name
        new_employee_obj.employee_status =  member_status_obj
        new_employee_obj.role            =  employee_role_obj
        new_employee_obj.report_to       =  report_to_obj
        new_employee_obj.save()

        for res in expert_list:
            experty_language = Experty.objects.get(id = res)
            new_employee_obj.experty.add(experty_language)
        return redirect("member")

    context = {
        'member_status':member_status,
        'member_role' : member_role,
        'report_to_employee':report_to_employee,
        'experty':experty
    }
    return render(request,'add_member.html',context)

@login_required(login_url='login')
def member_details(request,id):
    employee_obj       = EmployeeUser.objects.get(id = id)
    context = {
        'employee_obj':employee_obj
    }
    return render(request,'member_details.html',context)

@login_required(login_url='login')
def update_member(request,id):
    current_user = request.user
    if current_user.role.role == "Manager":
        employee_obj       = EmployeeUser.objects.get(id = id)
        objects_language = []
        for res in employee_obj.experty.all():
            objects_language.append(res.id)
        lookups = Q(role__role__icontains="Manager") | Q(role__role__icontains="Lead") | Q(is_active = True)
        report_to_employee = EmployeeUser.objects.filter(lookups).distinct().order_by("name")
        all_experty_language = Experty.objects.all().order_by("name")
        all_member_role      = EmployeeRole.objects.all()
        all_member_status    = EmployeeStatus.objects.all()

        if request.method == 'POST':
            name                       =   request.POST.get("employee_name")
            email                      =   request.POST.get("email")
            employee_status            =   request.POST.get("employee_status")
            password                   =   request.POST.get("password")
            report_to                  =   request.POST.get("report_to")
            experty                    =   request.POST.getlist('experty[]')
            employee_role              =   request.POST.get("employee_role")

            employee_status            =   EmployeeStatus.objects.get(id = employee_status)
            report_to                  =   EmployeeUser.objects.get(id = report_to)
            employee_role              =   EmployeeRole.objects.get(id  = employee_role)
            update_member_obj          = EmployeeUser.objects.filter(id = id).update(
                name                   = name,
                email                  = email,
                employee_status        = employee_status,
                report_to              = report_to,
                role                   = employee_role
            )
            update_member_obj          = EmployeeUser.objects.get(id = id)

            if update_member_obj:
                update_member_obj.set_password(password)
                update_member_obj.save()

            update_member_obj.experty.clear()
            for res in experty:
                experty_update = Experty.objects.get(id = res)
                update_member_obj.experty.add(experty_update)

            return redirect('member')

        context = {
            "employee_obj":employee_obj,
            "report_to_employee": report_to_employee,
            "objects_language_list":objects_language,
            "all_experty_language":all_experty_language,
            'all_member_role':all_member_role,
            'all_member_status':all_member_status
        }
        return render(request,'update_member.html',context)
    else:
        return redirect("login")


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect!'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def project(request):
    project_obj     = Project.objects.all()
    context = {
        'project_obj':project_obj
    }
    return render(request,'project.html',context)


@login_required(login_url='login')
def add_project(request):
    all_experty       =  Experty.objects.all()
    all_member           =  EmployeeUser.objects.all()
    if request.method == 'POST':
        project_name        =  request.POST.get('project_name')
        client_name         =  request.POST.get('client_name')
        start_date          =  request.POST.get('start_date')
        description         =  request.POST.get('description')
        experty             =  request.POST.getlist('experty[]')
        assign_user_list    =  request.POST.getlist('assign_user_list[]')

        project_obj         = Project.objects.create(
            name            = project_name,
            client_name     = client_name,
            start_date      = start_date,
            description     = description
        )
        for res in assign_user_list:
            assign_user        = EmployeeUser.objects.get(id = res)
            project_obj.assign_to.add(assign_user)

        for res in experty:
            experty_obj     = Experty.objects.get(id = res)
            project_obj.technology.add(experty_obj)
        return redirect("project")
    context = {
        'all_experty':all_experty,
        'all_member':all_member
    }
    return render(request,'add_project.html',context)


@login_required(login_url='login')
def project_details(request,id):
    project_obj     = Project.objects.get(id = id)
    context = {
        'project_obj':project_obj
    }
    return render(request,'project_details.html',context)

@login_required(login_url='login')
def delete_project(request,id):
    Project.objects.get(id = id).delete()
    return redirect("project")


@login_required(login_url='login')
def update_project(request,id):
    project_obj  = Project.objects.get(id = id)
    all_experty  = Experty.objects.all()
    all_member_user = EmployeeUser.objects.all()
    assign_member_list   = [res.id for res in project_obj.assign_to.all()]
    technoloty_list   = [res.id for res in project_obj.technology.all()]

    if request.method == 'POST':
        project_name        = request.POST.get('project_name')
        client_name         = request.POST.get('client_name')
        start_date          = request.POST.get('start_date')
        experty             = request.POST.getlist('experty[]')
        assign_project_user_list  = request.POST.getlist('assign_project_user_list[]')
        description         = request.POST.get('description')
        project_update_obj      = Project.objects.filter(id = id).update(
            name         = project_name,
            client_name  = client_name,
            start_date   = start_date,
            description  = description
        )
        project_obj.assign_to.clear()
        project_obj.technology.clear()
        for res in experty:
            experty_id  = Experty.objects.get(id = res)
            project_obj.technology.add(experty_id)
        for res in assign_project_user_list:
            user_id      = EmployeeUser.objects.get(id = res)
            project_obj.assign_to.add(user_id)
        return redirect('project')

    context = {
        'project_obj':project_obj,
        'all_experty':all_experty,
        'all_member_user':all_member_user,
        'assign_member_list':assign_member_list,
        'technoloty_list':technoloty_list
    }
    return render(request,'update_project.html',context)


def report(request):
    all_member          = EmployeeUser.objects.all()
    if request.method == 'POST':
        member_id       =  request.POST.get("member_id")
        start_date      =  request.POST.get("start_date")
        end_date        =  request.POST.get("end_date")
        member_obj      =  EmployeeUser.objects.get(id = member_id)
        task_obj        =  EmployeeTask.objects.filter(created_at__gte=start_date, created_at__lte=end_date, member = member_obj)
        print(task_obj)
    context = {
        'all_member':all_member
    }
    return render(request,'report.html',context)


def forgot_password(request):
    return render(request,'forgot_password.html')
