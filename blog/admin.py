from django.contrib import admin
from . import models


class FilterByTitle(admin.SimpleListFilter):
    title = "Most Visit"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            ("django", "DJANGO"),
            ("python", "PYTHON"),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


class CommentInline(admin.TabularInline):
    model = models.Comment


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("show_image", "title", "author", "created", "publish_at", "is_active")
    list_filter = ("is_active", FilterByTitle)
    search_fields = ("title", "body")
    inlines = (CommentInline,)
    # list_editable = ("is_active",)


admin.site.register(models.Category)
admin.site.register(models.Comment)
