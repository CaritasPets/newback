from django.contrib import admin
from .models import CommonUser, OrganizationUser
# Register your models here.
admin.site.register(CommonUser)
admin.site.register(OrganizationUser)