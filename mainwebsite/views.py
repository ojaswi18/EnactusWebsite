from django.shortcuts import render
from mainwebsite.models import Contact,Achievement,Member

# Create your views here.
def home(request):
    return render(request,"home.html")

def projects(request):
    return render(request,"projects.html")

def achievements(request):
    achievements=Achievement.objects.all()
    print(achievements)    
    context={'achievements':achievements}
    return render(request,"achievements.html",context)

def achievementsdetail(request,slug):
    achievementdetail=Achievement.objects.filter(slug=slug).first()
    print(achievementdetail.desc)
    context={"achievementdetail":achievementdetail}
    return render(request,"achievementsdetail.html",context)

def about(request):
    return render(request,'about.html')

def team(request):
    members=Member.objects.all()
    context={"members":members}
    return render(request,"team.html",context)

def contact(request):
    if( request.method=="POST" ):
        name=request.POST["name"]
        email=request.POST["email"]
        message=request.POST["message"]
        instance=Contact(name=name,email=email,message=message)
        instance.save()
        
        
    return render(request,"contact.html")