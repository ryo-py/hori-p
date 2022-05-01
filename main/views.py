from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

# contact us
def contact(request):
    return render(request, "contact.html")

# about
def about(request):
    return render(request, "about.html")

# service
def service(request):
    return render(request, "service.html")

# illustration
def illustration_gallary(request):
    return render(request, "illustration.html")


# 3d animation test
def test(request):
    return render(request, "test.html")

# scroll video test
def scroll_video(request):
    return render(request, "scroll_video.html")