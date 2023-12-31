from django.shortcuts import render , redirect
from django.http import FileResponse
import os
from django.conf import settings
from .models import *


# Create your views here.
def home(request):
    
    books = products.objects.filter(catagory__catagory_name = 'Books')[1:9]
    notes = products.objects.filter(catagory__catagory_name = 'Notes')[1:9]
    syllabus = products.objects.filter(catagory__catagory_name = 'Syllabus')[0:9]

    context = {
        'books':books , 
        'notes':notes , 
        'syllabus':syllabus
    }
    return render(request , 'home.html' , context)

def view_book(request , id):
    bookobj = products.objects.get(id = id)
    print(bookobj)
    return render(request , 'book_view.html' , {'book':bookobj} )


def books(request):
    books = products.objects.filter(catagory__catagory_name = 'Books')
    return render(request , 'book_catag.html' , {'books':books , 'heading':'Books'})


def notes(request):
    notes = products.objects.filter(catagory__catagory_name = 'Notes')
    return render(request , 'book_catag.html' , {'books':notes , 'heading':'Notes'})


def syllabus(request):
    syllabus = products.objects.filter(catagory__catagory_name = 'Syllabus')
    return render(request , 'book_catag.html' , {'books':syllabus , 'heading':'Syllabus'})

def download(request):
    if request.method == 'POST':
        id = request.POST.get('pid')
        bookobj = products.objects.get(id = id )
        count = int(bookobj.download_count)
        count+=1
        bookobj.download_count = str(count)
        bookobj.save()
        filepath = bookobj.bfile
        opened_file = open(os.path.join(settings.BASE_DIR , f'media/{str(filepath)}') , 'rb')
        return FileResponse(opened_file)