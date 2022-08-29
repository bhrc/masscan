from django.contrib import admin
from .models import Author, Content, Category, Type, Tag, Publication, Geotag
# Register your models here.
admin.site.register(Author),
admin.site.register(Content),
admin.site.register(Category),
admin.site.register(Type),
admin.site.register(Tag),
admin.site.register(Publication),
admin.site.register(Geotag),
