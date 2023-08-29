from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST
        title = data['mytitle']
        desc = data['desc']
        recepie_image = request.FILES.get('recepie_image')
        RecpieUpload.objects.create(title=title, description=desc, recepie_image=recepie_image)
        return redirect('/')
        # print()
    return render(request, 'index.html')

def view_rec(request):
    querySet = RecpieUpload.objects.all()
    context = {'dishes': querySet}
    return render(request, 'view_rec.html', context=context)

def aboutus(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def delete_rec(request, id):
    query = RecpieUpload.objects.get(id=id)
    query.delete()
    return redirect('/viewRecepies')
