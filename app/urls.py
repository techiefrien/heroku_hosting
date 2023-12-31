from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home , name='home') , 
    path('view-book\<str:id>' , views.view_book , name='view-book') , 
    path('Books' , views.books, name='books') , 
    path('Notes' , views.notes , name='notes') , 
    path('Syllabus' , views.syllabus , name='syllabus') , 
    path('download' , views.download , name='download')
]