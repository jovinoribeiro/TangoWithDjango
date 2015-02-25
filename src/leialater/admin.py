from django.contrib import admin
from django.contrib.auth.models import User

from leialater.models import Category, Bookmark

# Register your models here.
admin.site.register(Category)
admin.site.register(Bookmark)

