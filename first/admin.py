from django.contrib import admin
from .models import User,AdvisorModel,BookingAdvisorModel

# Register your models here.
admin.site.register(User)
admin.site.register(AdvisorModel)
admin.site.register(BookingAdvisorModel)

