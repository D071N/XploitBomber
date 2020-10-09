from django.contrib import admin

# Register your models here.

from .models import Attackinfo
from .models import Userinfo
from .models import Workerinfo


admin.site.register(Attackinfo)
admin.site.register(Userinfo)
admin.site.register(Workerinfo)