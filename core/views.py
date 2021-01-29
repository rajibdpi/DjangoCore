from django.shortcuts import render, HttpResponse
from mainapp.models import Conatct
# Create your views here.


def home(request):
    nameList = ['Rajib', 'Tanvir', 'Mamun']
    data = {
        'nameList': nameList,
    }
    return render(request, 'app.html', data)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        obj = Conatct(name=name, phone=phone, email=email)
        obj.save()
    return render(request, 'contact.html')
