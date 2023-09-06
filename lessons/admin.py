from django.contrib import admin
from .models import User, Topic, Lessons, Classes
# Register your models here.

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Lessons)
admin.site.register(Classes)
