from django.contrib import admin
from .models import Department,Employee,Leaves
# Register your models here.
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display=['id',"first_name",
#     'last_name' ,
#     'email' ,
#     'phone',
#     'department',
#     'position',
#     'date_hired']
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Leaves)

