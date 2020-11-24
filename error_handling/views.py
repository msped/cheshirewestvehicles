from django.shortcuts import render

# Create your views here.

def handler400(request, exception):
    return render(request, "400.html", status=400)

def handler403(request, exception):
    return render(request, "403.html", status=403)

def handler404(request, exception):
    return render(request, "404.html", status=404)

def handler500(request, *args, **argv):
    return render(request, "500.html", status=500) # install sentry near production for catching errors