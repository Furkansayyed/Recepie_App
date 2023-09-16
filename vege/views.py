from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
    if request.method == 'POST':
        data = request.POST
        title = data['mytitle']
        desc = data['desc']
        user = request.user
        recepie_image = request.FILES.get('recepie_image')
        RecpieUpload.objects.create(user=user, title=title, description=desc, recepie_image=recepie_image)
        messages.success(request, "The Recepie is addes Successfully...")
        return redirect('/')
        # print()
    return render(request, 'index.html')

@login_required(login_url='/accounts/login')
def view_rec(request):
    messages.info(request, "Hii Thanks for using me ....")
    querySet = RecpieUpload.objects.all()

    if request.GET.get('search'):
        querySet = querySet.filter(title__icontains = request.GET.get('search'))
    
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

def update_red(request, id):
    queryset = RecpieUpload.objects.get(id=id)
    context = {'dishes': queryset}

    if request.method == 'POST':
        data = request.POST
        title = data['mytitle']
        desc = data['desc']
        recepie_image = request.FILES.get('recepie_image')
        
        queryset.title = title
        queryset.description = desc

        if recepie_image:
            queryset.recepie_image = recepie_image

        queryset.save()
        messages.success(request, "Recepie Updated Successfully....")
        return redirect('/viewRecepies')

    return redirect('/viewRecepies')