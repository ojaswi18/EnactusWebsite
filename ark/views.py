from django.shortcuts import render
from ark.models import ArkInfo

# Create your views here.
def home(request):
    return render(request,"homeark.html")

def work(request):
    articles=ArkInfo.objects.all()
    context={"articles":articles}
    return render(request,"workark.html",context)

def patners(request):
    return render(request,"patnersark.html")

def more(request):
    return render(request,"moreark.html")