from django.shortcuts import render,redirect,get_object_or_404
from .models import Service, Contact,Indexmanage,Servicemanage,Contactmanage,Aboutmanage,User,About,Corevalue
from django.contrib import messages

# Create your views here.
def home(request):
    servicesdetails = Service.objects.all()
    contactdetails = Contact.objects.first()
    indexmanagedetails = Indexmanage.objects.first()
    return render(request, 'index.html',{'servicesdetails':servicesdetails,'contactdetails':contactdetails, 'indexmanagedetails':indexmanagedetails})

def services(request):
    servicesdetails = Service.objects.all()
    contactdetails = Contact.objects.first()
    servicemanagedetails = Servicemanage.objects.first()
    return render(request, 'services.html',{'servicesdetails':servicesdetails,'contactdetails':contactdetails,'servicemanagedetails':servicemanagedetails} )

def pricing(request):
    return render(request, 'pricing.html')

def about(request):
    corevaluedetails = Corevalue.objects.all()
    contactdetails = Contact.objects.first()
    aboutmanagedetails = Aboutmanage.objects.first()
    aboutdetails = About.objects.first()
    return render(request, 'about.html',{'contactdetails':contactdetails,
                                         'aboutdetails':aboutdetails,
                                          'aboutmanagedetails':aboutmanagedetails,
                                          'corevaluedetails': corevaluedetails
                                          } )

def contact(request):
    contactdetails = Contact.objects.first()
    contactmanagedetails = Contactmanage.objects.first()
    return render(request, 'contact.html' ,{'contactdetails':contactdetails, 'contactmanagedetails':contactmanagedetails,})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            if user.password == password:  # Plain-text password comparison
                request.session['user_id'] = user.id  # Store user ID in session
                messages.success(request, 'Successfully Logged-in.')
                return redirect('adminpanel')
            else:
                messages.error(request,'Invalid Password')
                return render(request, 'adminpanellogin.html')
        except User.DoesNotExist:
            messages.error(request,'User does not exist')
            return render(request, 'adminpanellogin.html')

    return render(request, 'adminpanellogin.html')



def admin_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']  # Remove user ID from session
    messages.success(request, 'Logged-out successfully.')
    return redirect('admin_login')


def adminpanel(request):
    if 'user_id' not in request.session:  # Check if user is logged in
        messages.error(request, 'You need to login.')
        return redirect('admin_login')
    servicesdetails = Service.objects.all()
    corevaluedetails = Corevalue.objects.all()
    contactdetails = Contact.objects.first() 
    aboutdetails = About.objects.first()
    indexmanagedetails = Indexmanage.objects.first()
    servicemanagedetails = Servicemanage.objects.first()
    aboutmanagedetails = Aboutmanage.objects.first()
    contactmanagedetails = Contactmanage.objects.first()
    

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'contact_form':
            if contactdetails:
             messages.error(request, "Contact details already exist. You can only edit or delete them.")
             return redirect('adminpanel')
            address = request.POST.get('address')
            email = request.POST.get('email')
            time = request.POST.get('time')
            phone = request.POST.get('phone')
            # Process contact form data (save to the database or perform other actions)
            Contact.objects.create(email=email,contnum=phone, address=address,timing=time)
            messages.success(request, 'Contact details updated')
            return redirect('adminpanel')

        elif form_type == 'service_form':
            name = request.POST.get('title')
            detail = request.POST.get('detail')
            icon_class = request.POST.get('icon_class', 'fas fa-cogs')  # Default icon
            Service.objects.create(name=name, detail=detail, icon_class=icon_class)
            messages.success(request, 'Service added')
            return redirect('adminpanel')
        
        elif form_type == 'about_form':
            if aboutdetails:
             messages.error(request, "About details already exist. You can only edit or delete them.")
             return redirect('adminpanel')
            story = request.POST.get('story')
            About.objects.create(story=story)
            messages.success(request, 'About information saved successfully.')
            return redirect(adminpanel)
        
        
        elif form_type == 'indexmanage_form':
            if indexmanagedetails:
             messages.error(request, "Index welcome details already exist. You can only edit or delete them.")
             return redirect('adminpanel')
            title = request.POST.get('wtitle')
            line = request.POST.get('wline')
            button_text = request.POST.get('wbtn')
            background_image = request.FILES.get('wimg')
            Indexmanage.objects.create(title=title, line=line, button_text=button_text, background_image=background_image)
            messages.success(request, 'Home page details saved successfully.')
            return redirect('adminpanel')
        
        elif form_type == 'servicemanage_form':
            if servicemanagedetails:
             messages.error(request, "Service welcome details already exist. You can only edit or delete them.")
             return redirect('adminpanel')
            title = request.POST.get('wtitle')
            line = request.POST.get('wline')
            button_text = request.POST.get('wbtn')
            background_image = request.FILES.get('wimg')
            Servicemanage.objects.create(title=title, line=line, button_text=button_text, background_image=background_image)
            messages.success(request, 'Service page details saved successfully.')
            return redirect('adminpanel')
        
        elif form_type == 'aboutmanage_form':
            if aboutmanagedetails:
             messages.error(request, "About welcome details already exist. You can only edit or delete them.")
             return redirect('adminpanel')
            title = request.POST.get('wtitle')
            line = request.POST.get('wline')
            button_text = request.POST.get('wbtn')
            background_image = request.FILES.get('wimg')
            Aboutmanage.objects.create(title=title, line=line, button_text=button_text, background_image=background_image)
            messages.success(request, 'About page details saved successfully.')
            return redirect('adminpanel')
        
        elif form_type == 'contactmanage_form':
            if contactmanagedetails:
             messages.error(request, "Contact welcome details already exist. You can only edit or delete them.")
             return redirect('adminpanel')
            title = request.POST.get('wtitle')
            line = request.POST.get('wline')
            button_text = request.POST.get('wbtn')
            background_image = request.FILES.get('wimg')
            Contactmanage.objects.create(title=title, line=line, button_text=button_text, background_image=background_image)
            messages.success(request, 'Contact page details saved successfully.')
            return redirect('adminpanel')
        
        elif form_type == 'corevalue_form':
            
            title = request.POST.get('title')
            detail = request.POST.get('detail')
            icon_class = request.POST.get('icon_class')
            Corevalue.objects.create(title=title, detail=detail, icon_class=icon_class)
            messages.success(request, 'Core value details saved successfully.')
            return redirect('adminpanel')

    return render(request, 'adminpanel.html', {'servicesdetails': servicesdetails,
                                               'contactdetails':contactdetails,
                                               'aboutdetails':aboutdetails,
                                                'indexmanagedetails':indexmanagedetails,
                                                'servicemanagedetails':servicemanagedetails,
                                                'aboutmanagedetails':aboutmanagedetails,
                                                'contactmanagedetails':contactmanagedetails,
                                                'corevaluedetails': corevaluedetails,
                                                })

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    messages.success(request, 'Service deleted successfully.')
    return redirect('adminpanel')  # Redirect to your admin panel or desired page

# def delete_contact(request, contact_id):
#     contact = get_object_or_404(Contact, id=contact_id)
#     contact.delete()

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        name = request.POST.get('title')
        detail = request.POST.get('detail')
        icon_class = request.POST.get('icon_class') 
        service.name = name
        service.detail = detail
        service.icon_class = icon_class
        service.save()

        messages.success(request, 'Service updated successfully.')
        return redirect('adminpanel')  # Redirect to your admin panel or desired page

    return render(request, 'edit_service.html', {'service': service})

def edit_about(request):
    aboutdetails = About.objects.first()
    if aboutdetails:
       if request.method == 'POST':
        aboutdetails.story = request.POST.get('story')
        aboutdetails.experience = request.POST.get('experience')
        aboutdetails.procom = request.POST.get('procom')
        aboutdetails.satisfaction = request.POST.get('satisfaction')
        aboutdetails.save()
        messages.success(request, 'About information Updated Successfully.')
        return redirect('adminpanel')
    else:
        messages.error(request, 'First add details')
        return redirect('adminpanel')
    return render(request, 'edit_about.html',{'aboutdetails':aboutdetails})

def delete_about(request):
    pass

def edit_contact(request):
    contact = Contact.objects.first()
    if contact: 
     if request.method == 'POST':
        # Manually update the fields from the POST data
        contact.address = request.POST.get('address')
        contact.email = request.POST.get('email')
        contact.contnum = request.POST.get('phone')
        contact.timing = request.POST.get('business_hours')

        # Save the updated contact
        contact.save()
        messages.success(request, 'Contact details updated successfully.')
        # Redirect after updating
        return redirect('adminpanel')  # Replace with your desired redirect
    else: 
        messages.error(request, 'First add contact details')
        return redirect('adminpanel')
    return render(request, 'edit_contact.html', {'contact': contact})

def delete_contact(request):
    contact = Contact.objects.first()  # Fetch the single contact
    print(contact)
    if contact:
        contact.delete()
        messages.success(request, "Contact details deleted successfully.")
    else:
        messages.error(request, "No contact details found to delete.")
    return redirect('adminpanel')

def edit_indexmanage(request):
    indexmanagedetails = Indexmanage.objects.first()

    if indexmanagedetails:
        if request.method == 'POST':
            indexmanagedetails.title = request.POST.get('wtitle')
            indexmanagedetails.line = request.POST.get('wline')
            indexmanagedetails.button_text = request.POST.get('wbtn')

            # Only update the image if a new one is uploaded
            if 'wimg' in request.FILES:
             indexmanagedetails.background_image = request.FILES.get('wimg')

            indexmanagedetails.save()
            messages.success(request, 'Index manage page details updated successfully.')
            return redirect('adminpanel')
        
    else:
            messages.error(request, 'First add details')
            return redirect('adminpanel')
        
    return render(request, 'edit_indexmanage.html',{'indexmanagedetails':indexmanagedetails})

def delete_indexmanage(request):
    indexmanagedetails = Indexmanage.objects.first()
    if indexmanagedetails:
        indexmanagedetails.delete()
        messages.success(request,'Index page details deleted successfully.')
        return redirect('adminpanel')
    
    else:
        messages.error(request,'No contact details found to delete.')
    return redirect('adminpanel')
    
def edit_servicemanage(request):
    servicemanagedetails = Servicemanage.objects.first()

    if servicemanagedetails:
        if request.method == 'POST':
            servicemanagedetails.title = request.POST.get('wtitle')
            servicemanagedetails.line = request.POST.get('wline')
            servicemanagedetails.button_text = request.POST.get('wbtn')

            # Only update the image if a new one is uploaded
            if 'wimg' in request.FILES:
             servicemanagedetails.background_image = request.FILES.get('wimg')

            servicemanagedetails.save()
            messages.success(request, 'Service manage page details updated successfully.')
            return redirect('adminpanel')
        
    else:
            messages.error(request, 'First add details')
            return redirect('adminpanel')
        
    return render(request, 'edit_servicemanage.html',{'servicemanagedetails':servicemanagedetails})

def delete_servicemanage(request):
    servicemanagedetails = Servicemanage.objects.first()
    if servicemanagedetails:
        servicemanagedetails.delete()
        messages.success(request,'service manage page details deleted successfully.')
        return redirect('adminpanel')
    
    else:
        messages.error(request,'No service manage details found to delete.')
    return redirect('adminpanel')

def edit_aboutmanage(request):
    aboutmanagedetails = Aboutmanage.objects.first()

    if aboutmanagedetails:
        if request.method == 'POST':
            aboutmanagedetails.title = request.POST.get('wtitle')
            aboutmanagedetails.line = request.POST.get('wline')
            aboutmanagedetails.button_text = request.POST.get('wbtn')

            # Only update the image if a new one is uploaded
            if 'wimg' in request.FILES:
             aboutmanagedetails.background_image = request.FILES.get('wimg')

            aboutmanagedetails.save()
            messages.success(request, 'About manage page details updated successfully.')
            return redirect('adminpanel')
        
    else:
            messages.error(request, 'First add details')
            return redirect('adminpanel')
        
    return render(request, 'edit_aboutmanage.html',{'aboutmanagedetails':aboutmanagedetails})

def delete_aboutmanage(request):
    aboutmanagedetails = Aboutmanage.objects.first()
    if aboutmanagedetails:
        aboutmanagedetails.delete()
        messages.success(request,'About manage page details deleted successfully.')
        return redirect('adminpanel')
    
    else:
        messages.error(request,'No about manage details found to delete.')
    return redirect('adminpanel')

def edit_contactmanage(request):
    contactmanagedetails = Contactmanage.objects.first()

    if contactmanagedetails:
        if request.method == 'POST':
            contactmanagedetails.title = request.POST.get('wtitle')
            contactmanagedetails.line = request.POST.get('wline')
            contactmanagedetails.button_text = request.POST.get('wbtn')

            # Only update the image if a new one is uploaded
            if 'wimg' in request.FILES:
             contactmanagedetails.background_image = request.FILES.get('wimg')

            contactmanagedetails.save()
            messages.success(request, 'Contact manage page details updated successfully.')
            return redirect('adminpanel')
        
    else:
            messages.error(request, 'First add details')
            return redirect('adminpanel')
        
    return render(request, 'edit_contactmanage.html',{'contactmanagedetails':contactmanagedetails})

def delete_contactmanage(request):
    contactmanagedetails = Contactmanage.objects.first()
    if contactmanagedetails:
        contactmanagedetails.delete()
        messages.success(request,'Contact manage page details deleted successfully.')
        return redirect('adminpanel')
    
    else:
        messages.error(request,'No contact manage details found to delete.')
    return redirect('adminpanel')

def edit_corevalue(request,id):
    corevaluedetails = get_object_or_404(Corevalue, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        icon_class = request.POST.get('icon_class') 
        corevaluedetails.title = title
        corevaluedetails.detail = detail
        corevaluedetails.icon_class = icon_class
        corevaluedetails.save()

        messages.success(request, 'Service updated successfully.')
        return redirect('adminpanel')  # Redirect to your admin panel or desired page
    return render(request, 'edit_corevalues.html', {'corevaluedetails':corevaluedetails})

def delete_corevalue(request,id):
    corevaluedetails = get_object_or_404(Corevalue, id=id)
    corevaluedetails.delete()
    messages.success(request, 'Core value deleted successfully.')
    return redirect('adminpanel')