from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Experty(models.Model):
    name             = models.CharField(max_length= 1000 , null = True , blank = True)
    created_at       = models.DateField(auto_now_add=True)
    status           = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class EmployeeRole(models.Model):
    role         = models.CharField(max_length = 100 , null = True , blank = True)

    def __str__(self):
        return self.role

class EmployeeStatus(models.Model):
    status = models.CharField(max_length = 100 , null = True , blank = True)

    def __str__(self):
        return self.status

class Department(models.Model):
    name    = models.CharField(max_length = 100 , null = True , blank = True)
    def __str__(self):
        return self.name


class EmployeeUser(AbstractUser):
    objects             = UserManager()
    username = None
    name                = models.CharField(max_length=1000, null=True, blank=True)
    birth_date          = models.DateField(null=True, blank=True)
    report_to           = models.ForeignKey("accounts.EmployeeUser", on_delete=models.CASCADE, null=True, blank=True)
    experty             = models.ManyToManyField(Experty, null=True, blank=True)
    role                = models.ForeignKey(EmployeeRole, on_delete=models.CASCADE, null=True, blank=True)
    department          = models.CharField(max_length=1000, null=True, blank=True, default="Engineering")
    employee_status     = models.ForeignKey(EmployeeStatus,on_delete=models.CASCADE, null=True, blank=True)
    email               = models.CharField(max_length=254, null=True, blank=True, unique=True )
    status              = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        # return str(self.phone_number) if self.phone_number else return str(self.username)
        if self.name:
            return str(self.name)
        else:
            "NA"




class Project(models.Model):
    name    = models.CharField(max_length = 1000 , null = True , blank = True)
    client_name    = models.CharField(max_length = 1000 , null = True , blank = True)
    description      = models.TextField(null = True , blank = True)
    created_at = models.DateField(auto_now_add=True)
    created_by  = models.ForeignKey(EmployeeUser,on_delete=models.CASCADE, null=True, blank=True)
    technology      = models.ManyToManyField(Experty, null=True, blank=True,related_name='project_Technology')
    assign_to      = models.ManyToManyField(EmployeeUser, null=True, blank=True,related_name='assign_to_member')
    start_date   = models.DateField(null = True, blank = True)
    end_date     = models.DateField(null = True , blank = True)

    def __str__(self):
        return self.name
class EmployeeProject(models.Model):
    project_name        = models.ForeignKey(Project ,on_delete=models.CASCADE, null = True , blank = True)
    employee_start_date = models.CharField(max_length= 1000 ,  blank=True, default='', null=True)
    employee_end_date   = models.CharField(max_length= 1000 , blank=True, default='', null=True)
    employee            = models.ForeignKey(EmployeeUser ,on_delete=models.CASCADE, null = True , blank = True)
    created_at          = models.DateField(auto_now_add=True )
    status              = models.BooleanField(default=True)

class TaskStatus(models.Model):
    task_status   = models.CharField(max_length=1000 , null = True , blank = True)

    def __str__(self):
        return self.task_status

class EmployeeTask(models.Model):
    task  = models.CharField(max_length=100 , null = True,blank=True)
    member = models.ForeignKey(EmployeeUser,on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project ,on_delete=models.CASCADE, null=True, blank=True)
    estimated_time = models.CharField(max_length=100 , null =  True, blank=True)
    actual_time = models.CharField(max_length= 100 , null = True , blank=True,default="0:0")
    task_status = models.ForeignKey(TaskStatus ,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(null = True, blank = True,auto_now_add=True)
    description = models.TextField(null = True, blank=True)

    def __str__(self):
        return self.description
