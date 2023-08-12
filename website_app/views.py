from django.shortcuts import render
from django.http import HttpResponse
from.forms import Student_form



# Create your views here.
def Web(request):
    return render(request,'proj.html')


def About(request):
    return render(request,'about.html')
def Course(request):
    return render(request,'allcourse.html')
def Call(request):
    return render(request,'call.html')
def Callus(request):
    return render(request,'callus.html')
def Join(request):
    return render(request,'join.html')
def Contact(request):
    return render(request,'contact.html')
def Getcall(request):
    if request.method=='POST':
        forms=Student_form(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse('Thankyou we will call back in 24 hours')
        else:
            return HttpResponse('data not added')
    else:
        forms=Student_form()
        return render(request,'getcall.html',{'forms':forms})
def Readmore(request):
    return render(request,'readmore.html')
