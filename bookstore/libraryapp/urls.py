from django.urls import path
from .views import *
urlpatterns = [
    path('' , home, name='home'),
    path('booklist',booklist,name='book-list'),
    path('addbook',addbook,name='add-book'),
    path('deletebook/<int:id>',deletebook,name='delete-book'),
    path('updatebook/<int:id>',updatebook,name='update-book'),

]