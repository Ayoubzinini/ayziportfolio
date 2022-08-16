from operator import concat
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contact

def index(request):
    concats = Contact.objects
    return render(request,'mycontacts/index.html',{'contacts':concats})
def details(request,contact_id):
    contact_details = get_object_or_404(Contact,pk=contact_id)
    return render(request,'mycontacts/details.html',{'contact':contact_details})