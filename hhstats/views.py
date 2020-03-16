from django.shortcuts import render


def stats_request(request):
    return render(request, 'stats-request.html')
