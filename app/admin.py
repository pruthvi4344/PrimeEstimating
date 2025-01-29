from django.contrib import admin
from .models import Service,Contact,About,Indexmanage,Servicemanage,Aboutmanage,Contactmanage,User
# Register your models here.
admin.site.register(User)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Indexmanage)
admin.site.register(Servicemanage)
admin.site.register(Aboutmanage)
admin.site.register(Contactmanage)
admin.site.register(About)
