from django.contrib import admin

from .models import TravelType ,Travel ,Question ,Choice , Traveluser

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(TravelType)
admin.site.register(Travel)
admin.site.register(Traveluser)