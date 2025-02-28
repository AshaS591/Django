from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Book



# Create your views here.
def home(request):
    q = request.GET.get('q','')
    if q:
        all_books = Book.objects.filter(title__contains=q)
    else:
        all_books = Book.objects.all()
    
    if all_books:
        context = {'all_books':all_books}
    else:
        context = {'msg':'Book Not available!!'}
        
    return render(request,'home.html',context)

def add_book(request):
     if request.method == 'POST':
        title = request.POST['title']
        authour = request.POST.get('authour','')
        genre = request.POST['genre']
        price = request.POST['price']
        published_date = request.POST['publish_date']
        description = request.POST['description']
        
        book = Book(
            title=title,
            authour=authour,
            genre=genre,
            price=price,
            published_date=published_date,
            description=description,
        )
        book.save()
        return redirect('home')
     return render(request,'add_book.html')

def edit_book(request,id):
    try:
        book = Book.objects.get(id=id)
    except:
        return HttpResponse('404 : Book Not Found')

    if request.method == 'POST':
        book.title = request.POST['title']
        book.authour = request.POST['authour']
        book.genre = request.POST['genre']
        book.price = request.POST['price']
        book.published_date = request.POST.get('published_date','2020-11-20')
        book.description = request.POST['description']
        book.save()
        return redirect('details', id=book.id)
    
    return render(request,'edit_book.html',{'book':book})
def delete_book(request,id):
    try:
        book=Book.objects.get(id=id)
        
    except:
        return HttpResponse('Book not available...')
    if request.method=='POST':
        book.delete()
        return redirect('home')
    return render(request,'delete_book.html',{'book':book})

def book_details(request, id):
    try:
        book = Book.objects.get(id=id)
    except:
        return HttpResponse('404 : Book Not Found')
    
    return render(request, 'book_details.html', {'book':book})