from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def blogdetails(request):
    return render(request, 'blog-details.html')

def portfoliodetails(request):
    return render(request, 'portfolio-details.html')

def servicedetails(request):
    return render(request, 'service-details.html')  

def starterpage(request):
    return render(request, 'starter-page.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')

