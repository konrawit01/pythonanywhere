from django.contrib import admin

from .models import Travel, TravelType, TravelPlaceKeeper

exit
admin.site.register(TravelType)
admin.site.register(Travel)
admin.site.register(TravelPlaceKeeper)