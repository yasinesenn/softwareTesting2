from django.contrib import admin

from Software.models import Author, BlogPost, Category, Comment, Industry, Tag

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted',)
    search_fields = ('title', 'author')
    list_filter = ('date_posted',)


admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Industry)
admin.site.register(Author)
admin.site.register(Comment)

