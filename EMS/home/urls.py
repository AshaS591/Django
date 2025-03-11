from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('detail/',views.details,name='detail'),
    path('leave/',views.leave_details,name='leave'),
    
    path('add/',views.add_employee,name='add_emp'),
    path('edit/<int:id>',views.edit_emp,name='edit'),
    # path('delete/',views.delete_emp,name='delete'),
    path('delete/<int:id>',views.confirm_delete,name='confirm'),
    path('apply/',views.apply_leave,name='apply'),




]