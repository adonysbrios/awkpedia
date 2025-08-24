from django.contrib import admin
from .models import Article, ActiveVersion, Publication

admin.site.register(Article)
admin.site.register(ActiveVersion)
admin.site.register(Publication)

# Register your models here.
