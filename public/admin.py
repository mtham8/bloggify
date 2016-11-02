from django.contrib import admin
from .models import Post

# To create a superuser for django admin ==> python manage.py createsuperuser
# Register your models here.
admin.site.register(Post)
