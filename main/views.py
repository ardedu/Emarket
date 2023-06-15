from django.shortcuts import render, HttpResponse
from users.models import Users

def home(request):
   return render(request, 'main/index.html')
# Create your views here.
def about(request):
   return render(request, 'main/about.html')
def contacts(request):
   return render(request, 'main/contacts.html')

def street(request):
    users = Users.objects.all()
    return render(request, 'main/street.html', {'users': users})
