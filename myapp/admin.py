# admin.py

from django.contrib import admin
from .models import College, School, UserProfile, CollegeRepresentative, SchoolRepresentative, UniqueID


class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'state')
    search_fields = ('name', 'district', 'state')
    list_filter = ('state', 'district')

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'state')
    search_fields = ('name', 'district', 'state')
    list_filter = ('state', 'district')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'state', 'district', 'college', 'school', 'year_of_study', 'representative_type', 'unique_id')
    search_fields = ('name', 'phone', 'state', 'district', 'college__name', 'school__name')
    list_filter = ('representative_type', 'state', 'district')

class CollegeRepresentativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'state', 'district', 'college', 'unique_id')
    search_fields = ('name', 'phone', 'state', 'district', 'college__name')
    list_filter = ('state', 'district')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(representative_type='college')

class SchoolRepresentativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'state', 'district', 'school', 'unique_id')
    search_fields = ('name', 'phone', 'state', 'district', 'school__name')
    list_filter = ('state', 'district')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(representative_type='school')
class UniqueIDAdmin(admin.ModelAdmin):
    list_display = ('representative_type', 'unique_id', 'is_used')
    search_fields = ('unique_id', 'representative_type')
    list_filter = ('representative_type', 'is_used')


# Register models with admin site
admin.site.register(College, CollegeAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CollegeRepresentative, CollegeRepresentativeAdmin)
admin.site.register(SchoolRepresentative, SchoolRepresentativeAdmin)
admin.site.register(UniqueID, UniqueIDAdmin)
