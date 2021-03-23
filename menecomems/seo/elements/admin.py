from django.contrib import admin
from .models import Element, Attribute, Key, Tag


# Register your models here.
class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 1


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    inlines = [AttributeInline]
    list_display = ('name', 'tag',)
    list_filter = ('tag',)
    search_fields = ('name',)


admin.site.register(Tag)
admin.site.register(Key)