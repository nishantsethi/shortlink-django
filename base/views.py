from django.shortcuts import render
from django.http import HttpResponse
from base.models import Urls
from django.shortcuts import redirect
from . import forms
import random
import string
import re




def index(request):
    form = forms.UrlInput()
    short_url_code = ""
    #Check to see if we are getting a POST request back
    if request.method == "POST":
    # if post method = True
        form = forms.UrlInput(request.POST)

    # Then we check to see if the form is valid (this is an automatic  validation by Django)
        if form.is_valid():
        # if form.is_valid == True then do something
            print("Form validation successful! See console for information:")
            print("Name: "+form.data['long_url'])

            short_url_code = ''.join(random.choices(string.ascii_lowercase, k = 5))

            while Urls.objects.filter(short_url = short_url_code).exists():
                short_url_code = ''.join(random.choices(string.ascii_lowercase, k =5))
            else:
                obj = Urls.objects.create(long_url=form.data['long_url'], short_url=short_url_code)
                obj.save()

    return render(request, 'base/index.html', {'form':form, 'short_code' : short_url_code})
        

def redirector(request, uri):

    def formaturl(url):
        if not re.match('(?:http|https)://', url):
            return 'http://{}'.format(url)
        return url

    try:
        url = Urls.objects.get(short_url=uri)

        long_url = formaturl(url.long_url)



        return redirect(long_url)

    except:
        return HttpResponse("Short Link not found")

