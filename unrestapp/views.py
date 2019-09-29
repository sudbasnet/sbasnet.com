from django.shortcuts import render


def unrestapp(request):
    return render(request, 'unrestapp/map.html')
