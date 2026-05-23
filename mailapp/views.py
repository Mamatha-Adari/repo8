from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.mail import send_mail
from .forms import EmailMessageForm

def send_email_view(request):
    if request.method == "POST":
        form = EmailMessageForm(request.POST)
        if form.is_valid():
            email_obj = form.save()  
            send_mail(
                subject=email_obj.subject,
                message=email_obj.message,
                from_email="adarimamatha561@gmail.com",
                recipient_list=["mamathaadarias@gmail.com"],
                fail_silently=False,
            )
            return HttpResponse("<h1>Succesfully sent mail  </h1>")
    else:
        form = EmailMessageForm()
    return render(request, "mailapp/send_mail.html", {"form": form})

