from django.contrib import admin

from posts.models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'image', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value = '-пусто-'


admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Group)
