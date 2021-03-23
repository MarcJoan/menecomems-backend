from django.contrib import admin
from .models import Robot, URL, UserAgent, Rule


# Register your models here.
class RuleInline(admin.TabularInline):
    model = Rule
    extra = 1


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    inlines = [RuleInline]
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(UserAgent)
admin.site.register(URL)
