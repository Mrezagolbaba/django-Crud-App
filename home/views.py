from django.shortcuts import render
from .models import Todo


# Create your views here.
def send_email(request):
    person={'name':'reza','code':'1234321'}
    return render(request,'email.html', context=person)

def home(request):
    todos= Todo.objects.all()
    return render(request ,'home.html',{'todos':todos})