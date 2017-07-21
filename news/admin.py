# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *


class NewInline(admin.TabularInline):
    extra = 1
    model = New


class CategoryNewsAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    inlines = [NewInline,]


admin.site.register(New)
admin.site.register(CategoryNews, CategoryNewsAdmin)
