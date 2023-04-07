from django.shortcuts import render
from khoj.models import KhojInfo

# Create your views here.
def home(request):
    return render(request,"homekhoj.html")

def work(request):
    articles=KhojInfo.objects.all()
    context={"articles":articles}
    return render(request,"workkhoj.html",context)

def patners(request):
    return render(request,"patnerskhoj.html")

def more(request):
    return render(request,"morekhoj.html")