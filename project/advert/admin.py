from django.contrib import admin
from .models import Category, Post, Reaction


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Reaction)
