from django.contrib import admin
from .models import CSOEvent, MitigationAction

admin.site.register(CSOEvent)
admin.site.register(MitigationAction)
