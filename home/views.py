from django.shortcuts import render


# Create your views here.
def send_email(request):
    person={'name':'reza','code':'1234321'}
    return render(request,'email.html', context=person)