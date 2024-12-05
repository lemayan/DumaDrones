from django.shortcuts import render, redirect
from .models import Member, Contact



# Create your views here.

def index(request):
    if request.method=='POST':
        if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password'] ).exists():
             members = Member.objects.get(
                 username=request.POST['username'],
                 password=request.POST['password'])
             return render(request,'index.html',{'members':members})
        else:
             return render(request,'login.html')
    else:
        return render(request,'login.html')

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
    if request.method == 'POST':
        all = Contact(name=request.POST['name'],
                      email=request.POST['email'],
                      subject=request.POST['subject'],
                      message=request.POST['message']
                      )
        all.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')
def register(request):
    if request.method=='POST':
        members= Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        members.save()
        return redirect('/login')
    else:
        return render(request,'register.html')
    
