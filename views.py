from django.shortcuts import render
from django.http import HttpResponse
from .models import MailList
from django.conf import settings
from django.urls import reverse
from .forms import NameForm


# Create your views here.

def index(request):

   
    mailList = MailList() 
    mailList.status = "hidden"


    
    if request.method == 'POST' : 

        form = NameForm(request.POST)

        error_messages = None
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            post_data = request.POST.copy()
            email = post_data.get('email')


            if MailList.objects.filter(email = email).exists()  : 
                mailList.status = "hidden"

            else :
                mailList.email = email 
                mailList.status = "success"
                mailList.save()
            
            return render(request, "index.html", {"mailList": mailList,"form": NameForm() })
        else :
            post_data = request.POST.copy()
            mailList.status = "error"
            mailList.invalid_mail = post_data.get('email')
            #raise ValidationError(_("Invalid value: %(value)s"),code="invalid",params={"value": "42"},)
            return render(request, "index.html", {"form": form, "mailList" : mailList })
        #HttpResponseRedirect(reverse('index'))

    else:
        form = NameForm()

    return render(request, "index.html", {"form": form})



