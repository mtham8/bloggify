from django.contrib import admin
from .models import Post
from .models import Comment

# To create a superuser for django admin ==> python manage.py createsuperuser
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
