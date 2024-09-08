from django.shortcuts import render

def fun(request):
    return render(request,'home.html')
def yup(request):
    return render(request,'home2.html')
# Create your views here.
