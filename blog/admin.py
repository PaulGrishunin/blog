from django.contrib import admin
from .models import Post
from .models import Tag
from .models import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "slug", 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    # Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
