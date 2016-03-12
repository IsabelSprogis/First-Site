#12/03/2016
#@Author Isabel Sprogis
# Django site tutorial

from django.contrib import admin
from .models import Post

admin.site.register(Post)