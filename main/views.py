from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

# contact us
def contacts(request):
    return render(request, "contact.html")

# about
def company(request):
    return render(request, "about.html")

# illustration
def company(request):
    return render(request, "illustration_gallary.html")
