
from django.contrib import admin
from .models import * # Import your model

# Register your model
admin.site.register(Client)
admin.site.register(Project)
