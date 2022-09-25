from django.contrib import admin
from annonces.models import Category,Subcategory,Annonce,ATO
# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Annonce)
admin.site.register(ATO)