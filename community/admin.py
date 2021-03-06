from django.contrib import admin

from .models import Link, Photo, Post, Video
from cms.admin import ContentManageableModelAdmin, ContentManageableStackedInline


class LinkInline(ContentManageableStackedInline):
    model = Link
    extra = 0


class PhotoInline(ContentManageableStackedInline):
    model = Photo
    extra = 0


class VideoInline(ContentManageableStackedInline):
    model = Video
    extra = 0


class PostAdmin(ContentManageableModelAdmin):
    date_hierarchy = 'created'
    list_display = ['__str__', 'status', 'media_type']
    list_filter = ['status', 'media_type']
    inlines = [
        LinkInline,
        PhotoInline,
        VideoInline,
    ]


class PostTypeAdmin(ContentManageableModelAdmin):
    date_hierarchy = 'created'
    raw_id_fields = ['post']


admin.site.register(Post, PostAdmin)
admin.site.register(Link, PostTypeAdmin)
admin.site.register(Photo, PostTypeAdmin)
admin.site.register(Video, PostTypeAdmin)
