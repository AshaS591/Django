from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    if request.method == 'POST':
        name = request.POST.get('tname','')
        desc = request.POST.get('desc','')

        Task.objects.create(
            tname=name,
            tdesc=desc,
            tuser=request.user
        )
        return redirect('home1')
    
    tasks = Task.objects.filter(tuser=request.user)
    context={'tasks':tasks}
    return render(request,'home.html',context)

def update_task(request,pk):
    context={}
    try:
        task= Task.objects.get(id=pk,tuser=request.user) # tuser is used to give access to only authorised user -->he can access only his records

        context['task']=task
    except:
        context['error']='Task Not Found!!'
    
    if request.method == 'POST':
        task.tname=request.POST.get('tname')
        task.tdesc=request.POST.get('desc')
        task.save()
        return redirect('home1')

    return render(request,'update.html',context)

def delete_task(request,pk):
    context={}
    try:
        task= Task.objects.get(id=pk,tuser=request.user) # tuser is used to give access to only authorised user -->he can access only his records

        context['task']=task
    except:
        context['error']='Task Not Found!!'
    if request.method=='POST':
        task.delete()
        return redirect('home1')

    return render(request,'confirm.html')
    
