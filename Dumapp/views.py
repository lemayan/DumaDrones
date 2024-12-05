from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from .credentials import LipanaMpesaPpassword, MpesaAccessToken
from .models import Member, Contact, ImageModel
from .forms import ImageUploadForm



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


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Sending a drone your way!"  
            return redirect('show_images')  
        else:
            return render(request, 'upload_image.html', {'form': form, 'error': 'Please correct the errors below.'})
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_images(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def delete_image(request, pk):
    image = get_object_or_404(ImageModel, pk=pk)
    image.delete()
    return redirect('show_images')


def edit_image(request, pk):
    image = get_object_or_404(ImageModel, pk=pk)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('show_images')  
    else:
        form = ImageUploadForm(instance=image)
    return render(request, 'edit_image.html', {'form': form, 'image': image})

def pay_package(request):
    package = request.GET.get('package', '')
    amount = request.GET.get('amount', '0')
    return render(request, 'pay_package.html', {'package': package, 'amount': amount})



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "DumaDrones",
            "TransactionDesc": "Drone Delivery Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Payment Successfull")


def token(request):
    consumer_key = 'yXTSEKgOJp9iuNojQATROKhgI7IoXVUpZs6t8bAFkT8CPLmd'
    consumer_secret = 'Ytp0H4azuvNa5Rsh6S6oi0lkAUuqrjmdJyoNckp52hxgOA8rFZoiiAdLeKGSkHqb'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})