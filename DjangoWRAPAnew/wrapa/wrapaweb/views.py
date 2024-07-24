from django.shortcuts import render

# Create your views here.
def Index(request):

    return render(request, 'wrapaweb/Index.html')

def About(request):

    return render(request, 'wrapaweb/About.html')

def Contact(request):

    return render(request, 'wrapaweb/Contact.html')

def Deworming(request):

    return render(request, 'wrapaweb/Deworming.html')

def Rollback(request):

    return render(request, 'wrapaweb/Rollback.html')