from django.contrib import admin

from law.models import UserProfile, ProfessionalCategory, Professional, Location

# Register your models here.

admin.site.register(UserProfile)

admin.site.register(Professional)
admin.site.register(ProfessionalCategory)
admin.site.register(Location)
