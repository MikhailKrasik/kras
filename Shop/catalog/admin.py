from django.contrib import admin

from .models import Author, Seria, PublishingHouse, Genre

admin.site.register(Author)
admin.site.register(Seria)
admin.site.register(PublishingHouse)
admin.site.register(Genre)

