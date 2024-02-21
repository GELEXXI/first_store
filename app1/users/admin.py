from django.contrib import admin
from users.models import User
# Register your models here.

admin.site.register(User)


# @admin.register(User)
# class CategoriesAdmin(admin.ModelAdmin):
#     prepopulated_fields={'slug':('name',)}