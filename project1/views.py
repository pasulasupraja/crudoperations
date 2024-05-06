from django.shortcuts import render

from crud.models import Student


def crud(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request,"crud.html",context)

def about(request):
    return render(request,"about.html")