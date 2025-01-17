from django.contrib import admin
from .models import Post,Comment,Tag, AuthorProfile

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(AuthorProfile)