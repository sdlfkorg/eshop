from django.shortcuts import render
from .models import Sausage
# Create your views here.

def home(request):
    sausage_list = Sausage.objects.all()
    content = {
    "sausage_list": sausage_list,
    }
    
    return render(request, "home.html", content)