from django.shortcuts import render

# Create your views here.
def asd(request):
    return render(request, 'main.html', {'': 1,})