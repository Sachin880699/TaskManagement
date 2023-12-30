from django.urls import path
from.import views

urlpatterns = [
    path("home",views.home,name='home'),
    path("",views.task,name = 'task'),
    path("member",views.member, name = 'member'),
    path('add_member',views.add_member,name = 'add_member'),
    path("member_details/<int:id>",views.member_details,name='member_details'),
    path("update_member/<int:id>",views.update_member,name='update_member'),
    path("login",views.login , name = 'login'),
    path('project',views.project, name='project'),
    path("add_project",views.add_project,name = 'add_project'),
    path("project_details/<int:id>",views.project_details,name='project_details'),
    path("delete_project/<int:id>",views.delete_project , name = 'delete_project'),
    path("update_project/<int:id>",views.update_project,name = 'update_project'),
    path("logout",views.logout,name = 'logout'),
    path("create_task",views.create_task,name = 'create_task'),
    path("task_details/<int:id>",views.task_details , name='task_details'),
    path("update_task/<int:id>",views.update_task, name = 'update_task'),
    path("report",views.report, name = 'report'),
    path("forgot_password",views.forgot_password,name = 'forgot_password')

]
