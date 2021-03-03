from django.contrib import admin
from .models import image,Video,Naruto,Demonslayer

class imageAdmin(admin.ModelAdmin):
    list_display=['name','date','image']
    list_filter=['date','feedback']
admin.site.register(image,imageAdmin)
# Register your models here.
admin.site.register(Video)
admin.site.register(Naruto)
admin.site.register(Demonslayer)
