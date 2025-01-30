from django.contrib import admin
from .models import Service,Contact,Indexmanage,Servicemanage,Aboutmanage,Contactmanage,User,About,Corevalue
# Register your models here.
admin.site.register(User)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Indexmanage)
admin.site.register(Servicemanage)
admin.site.register(Aboutmanage)
admin.site.register(Contactmanage)
admin.site.register(About)
admin.site.register(Corevalue)
