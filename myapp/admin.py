from django.contrib import admin
from .models import UserProfile, College

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'state', 'district', 'college', 'year_of_study')
    search_fields = ('name', 'phone', 'state', 'district', 'college', 'year_of_study')
    list_filter = ('state', 'district', 'year_of_study', 'college')

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)