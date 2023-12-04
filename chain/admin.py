from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from chain.models import Chain

# Register your models here.

admin.site.register(Chain, MPTTModelAdmin)
