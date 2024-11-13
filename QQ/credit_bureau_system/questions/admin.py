from django.contrib import admin
from .models import UserResponse, Question

# Register your models here.
admin.site.register(Question)
admin.site.register(UserResponse)
