from django.shortcuts import render

from core.forms import ContactForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})