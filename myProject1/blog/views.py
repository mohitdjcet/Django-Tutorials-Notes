from django.http import HttpResponse

def home(request):
    return HttpResponse("Blog Home Page")

def about(request):
    return HttpResponse("Blog About Page")