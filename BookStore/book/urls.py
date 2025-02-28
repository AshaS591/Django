from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add_book,name='addbook'),
    path('edit/<int:id>',views.edit_book,name='edit'),
    path('delete/<int:id>',views.delete_book,name='delete'),
    path('details/<int:id>',views.book_details,name='details'),

]