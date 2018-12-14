from django.contrib import admin
from .models import Metrics
from .models import Users
from .models import Tracks
from .models import Teams

admin.site.register(Metrics)
admin.site.register(Teams)
admin.site.register(Tracks)
admin.site.register(Users)
