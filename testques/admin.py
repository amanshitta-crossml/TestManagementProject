from django.contrib import admin
from .models import Question, Option, Group

# Register your models here.

"""
registering models with the project
so that admin can view and edit from panel
"""

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Group)