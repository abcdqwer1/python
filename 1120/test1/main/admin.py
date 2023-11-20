from django.contrib import admin
from .models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at']
    list_display_links = ['title']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    list_per_page = 10