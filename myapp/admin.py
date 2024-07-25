from django.contrib import admin
from .models import UserProfile, College, CollegeRepresentative, SchoolRepresentative

class CollegeRepresentativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'state', 'district', 'college', 'year_of_study')
    search_fields = ('name', 'phone', 'state', 'district', 'college', 'year_of_study')
    list_filter = ('state', 'district', 'year_of_study', 'college')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(representative_type='college')

class SchoolRepresentativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'state', 'district', 'school', 'year_of_study')
    search_fields = ('name', 'phone', 'state', 'district', 'school', 'year_of_study')
    list_filter = ('state', 'district', 'year_of_study', 'school')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(representative_type='school')

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(CollegeRepresentative, CollegeRepresentativeAdmin)
admin.site.register(SchoolRepresentative, SchoolRepresentativeAdmin)
