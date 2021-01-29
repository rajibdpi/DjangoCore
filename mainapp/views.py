from django.shortcuts import render, HttpResponsePermanentRedirect

# Create your views here.


def other(request):
    otherList = ["apple", "banana", "cherry"]
    data = {'otherList': otherList}
    return render(request, 'other.html', data)
