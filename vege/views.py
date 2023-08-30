from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def registerUsers(request):

    if request.method == 'POST':
        firstName = request.POST.get('fname')
        LastName = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('passwd')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Username not available")
            return redirect('/register')
            # return redirect(request, '/register')

        user = User.objects.create(
            first_name = firstName,
            last_name = LastName,
            username = username
        )

        user.set_password(password)
        user.save()
        messages.success(request, "Account Created Successfully....")

        return redirect('/register')

    return render(request, 'register.html')

def loginUsers(request):
    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        data = request.POST
        title = data['mytitle']
        desc = data['desc']
        recepie_image = request.FILES.get('recepie_image')
        RecpieUpload.objects.create(title=title, description=desc, recepie_image=recepie_image)
        messages.success(request, "The Recepie is addes Successfully...")
        return redirect('/')
        # print()
    return render(request, 'index.html')

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
        return redirect('/viewRecepies')

    return render(request, 'update-rec.html', context)