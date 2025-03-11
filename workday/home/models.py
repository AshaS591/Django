from django.db import models

# Create your models here.
class Department(models.Model):
    dname = models.CharField(max_length=50)
    loc=models.CharField(max_length=50)

    def __str__(self):
        return self.dname


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    date_hired = models.DateField()
    
    def __str__(self):
        return self.first_name

class Leaves(models.Model):
    type = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    no_of_days = models.IntegerField(max_length=2)
    approved = models.BooleanField(null=True)
    emp_id = models.OneToOneField(Employee,on_delete=models.CASCADE)
    def __str__(self):
        return self.type