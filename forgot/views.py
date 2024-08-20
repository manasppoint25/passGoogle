from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def forgot(request):
    email = request.POST['email']
    subject = 'Password Changing Process'
    message = 'Please follow the instructions to change your password.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]

    
    send_mail(subject, message, email_from, recipient_list)
    
    return render(request, 'passcheck.html')

def confirm(request):
    pwd = request.POST['pwd']
    cpwd = request.POST['cpass']
    msg = ''
    
    if pwd == cpwd:
        msg = 'Password matches'
        return render(request, 'index.html', {'msg': msg})
    else:
        msg = 'Passwords do not match'
    
    
