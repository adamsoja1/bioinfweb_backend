from django.contrib import admin
from .models import Post, Comment, Multimedia, Galery, Tags
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Multimedia)
admin.site.register(Galery)
admin.site.register(Tags)