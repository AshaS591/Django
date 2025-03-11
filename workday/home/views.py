from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Department,Employee, Leaves
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):  
    return render(request,'home_page.html')

def edit_emp(request,id):
    try:
        employee = Employee.objects.get(id=id)
        departments = Department.objects.all()  # Retrieve all employee

    except:
        return HttpResponse('404 : Employee Not Found')

    if request.method == 'POST':
        employee.first_name = request.POST['first_name']
        employee.last_name = request.POST['last_name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.position = request.POST['position']
        employee.date_hired = request.POST['date_hired']
        employee.department_id = request.POST['department']
        employee.department = Department.objects.get(id=employee.department_id) # type: ignore
        employee.save()
        return redirect('detail')
    
    return render(request, 'edit.html', {'employee': employee, 'departments':departments})
    

def details(request):
    q = request.GET.get('q','')
    if q:
        all_employees = Employee.objects.filter(title__contains=q)
    else:
        all_employees = Employee.objects.all()
    
    if all_employees:
        context = {'all_employees':all_employees}
    else:
        context = {'msg':'Employee Not available!!'}

    return render(request,'deatails.html',context)

def add_employee(request):
    departments = Department.objects.all()  # Fetch all employee
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department_id = request.POST.get('department')
        position = request.POST.get('position')
        date_hired = request.POST.get('date_hired')

        department = Department.objects.get(id=department_id)

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            department=department,
            position=position,
            date_hired=date_hired,
            tuser=request.user
        )
        return redirect('detail')

    return render(request,'add_employee.html', {'departments': departments})

        
def confirm_delete(request,id):
    
    try:
        employee=Employee.objects.get(id=id)
        
    except:
        return HttpResponse('Employee not available...')
    
    print(f"Employee ID: {id}, Found Employee: {employee}")

    if request.method=='POST':
        employee.delete()
        return redirect('detail')
        
    return render(request,'delete_emp.html',{'employee':employee})

def apply_leave(request):
    if request.method=='POST':
        leave_type= request.POST.get('type','')
        from_date = request.POST.get('from_date','')
        to_date =request.POST.get('to_date','')
        no_days=request.POST.get('days','')
        approve=request.POST.get('approve','')
        ename=request.POST.get('emp_id','')
        employee = Employee.objects.get(id=ename)


        Leaves.objects.create(
            type =leave_type,
            from_date=from_date,
            to_date=to_date,
            no_of_days=no_days,
            approved=approve,
            emp_id=employee[1]+employee[2]
        )
        return redirect('leave')
    
    return render(request,'apply_leave.html')


def leave_details(request):
    all_leaves = Leaves.objects.all()
    
    if all_leaves:
        context = {'all_leaves':all_leaves}
    else:
        context = {'msg':'Leave details Not available!!'}
        
    return render(request,'leave.html',context)