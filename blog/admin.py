from django.contrib import admin
from .models import Post

admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "slug", 'status', 'created_on')
# Register your models here.