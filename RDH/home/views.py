from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Contact, Agent
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

@login_required(login_url='/accounts/login/')
def add_property(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        property_type = request.POST.get('property_type')
        image = request.FILES.get('image')
        beds = request.POST.get('beds')
        baths = request.POST.get('baths')
        area = request.POST.get('area')
        location = request.POST.get('location')
        owner = request.POST.get('owner')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        price = request.POST.get('price')
        description = request.POST.get('description', '')

        Property.objects.create(
            user=request.user,
            title=title,
            property_type=property_type,
            image=image,
            beds=beds,
            baths=baths,
            area=area,
            location=location,
            owner=owner,
            email=email,
            phone=phone,
            price=price,
            description=description
        )
        return redirect('property_type', property_type=property_type)  

    return render(request, 'add_property.html')


def CA_view(request):
    agents = Agent.objects.all()
    return render(request, 'C.A.html', {'agents': agents})

def CA_proUI_view(request):
    return render(request, 'proUI.html')

def home_view(request):
    return render(request, 'home.html')

def properties_view(request):
    return render(request, 'proUI.html')

def marla_5_view(request):
    properties = Property.objects.filter(property_type='5_MARLA')
    return render(request, '5-Marla.html', {'properties': properties})

def marla_7_view(request):
    properties = Property.objects.filter(property_type='7_MARLA')
    return render(request, '7-Marla.html', {'properties': properties})

def marla_10_view(request):
    properties = Property.objects.filter(property_type='10_MARLA')
    return render(request, '10-marla.html', {'properties': properties})

def kanal_view(request):
    properties = Property.objects.filter(property_type='1_KANAL')
    return render(request, '1-kanal.html', {'properties': properties})

def terms_view(request):
    return render(request, 'Term_and_Condition.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email-contact')
        phone = request.POST.get('contact number')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        # Send email notification
        send_mail(
            subject=f'New Contact from {name}',
            message=f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],  # Send to the site admin email
            fail_silently=False,
        )
        return render(request, 'con4.html', {'success': True})
    return render(request, 'con4.html')


def property_type_view(request, property_type):
    properties = Property.objects.filter(property_type=property_type)
    template_map = {
        '5_MARLA': '5-Marla.html',
        '7_MARLA': '7-Marla.html',
        '10_MARLA': '10-marla.html',
        '1_KANAL': '1-kanal.html',
    }
    template_name = template_map.get(property_type, 'proUI.html')
    return render(request, template_name, {'properties': properties})


@login_required(login_url='/accounts/login/')
def update_property_status(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    if property_obj.user != request.user:
        return HttpResponseForbidden('You are not allowed to update this property.')
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Property.STATUS_CHOICES):
            property_obj.status = new_status
            property_obj.save()
            return redirect('property_type', property_type=property_obj.property_type)
    return render(request, 'update_property_status.html', {'property': property_obj})

@login_required(login_url='/accounts/login/')
def delete_property(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    if property_obj.user != request.user:
        return HttpResponseForbidden('You are not allowed to delete this property.')
    if request.method == 'POST':
        redirect_type = property_obj.property_type
        property_obj.delete()
        return redirect('property_type', property_type=redirect_type)
    return render(request, 'delete_property_confirm.html', {'property': property_obj})

def property_search_view(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    property_type = request.GET.get('property_type')
    properties = Property.objects.all()
    if property_type:
        properties = properties.filter(property_type=property_type)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    return render(request, 'property_results.html', {'properties': properties})

def property_detail_view(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property_detail.html', {'property': property})