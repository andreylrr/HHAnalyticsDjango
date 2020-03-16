from django.shortcuts import render

def hhrequest(request):
    return render(request, 'requests.html')

def history(request):
    return render(request, 'history.html')


