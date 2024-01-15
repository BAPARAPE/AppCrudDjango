from django.http import HttpResponse
from django.shortcuts import render, redirect

from etud.forms import Student
from etud.models import User


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        created, user = User.objects.get_or_create(name=name,
                                                   email=email,
                                                   password=password)
        if not created:
            return HttpResponse("Cet etudiant existe déja")
        fm = Student()
    else:
        fm = Student()
    stud = User.objects.all()
    return render(request, 'etud/home.html', context={'form':fm, 'stu':stud})

def update_data(request, id):
    if request.method == "POST":
        name = request.POST("name")
        email = request.POST("email")
        password = request.POST("password")
        pi = User.objects.get(id=id)
        pi.name = name
        pi.email = email
        pi.password = password
        pi.save()
        return redirect('index')
    else:
        pi = User.objects.get(id=id)
        fm = Student(instance=pi)
    return render(request, 'etud/update.html', context={'form':fm})

def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(id=id)
        pi.delete()
        return redirect('index')
