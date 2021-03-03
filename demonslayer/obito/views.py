from django.shortcuts import render
from .forms import imageform
from .models import image
from .models import Video,Naruto,Demonslayer


# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):

    return render(request,'about.html')
def onepiece(request):
    video=Video.objects.all()
    return render(request,'onepiece.html',{'video':video})
def naruto(request):
    video=Naruto.objects.all()
    return render(request,'naruto.html',{'video':video})
def demonslayer(request):
    video=Demonslayer.objects.all()
    return render(request,'demonslayer.html',{'video':video})
def contact(request):
    if request.method=='POST':
        form=imageform(request.POST,request.FILES)

        if form.is_valid():

            form.save()

    form=imageform()

    return render(request,'contact.html',{'form':form})
