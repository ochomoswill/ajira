from django.contrib import admin
from .models import Countries, Counties, Constituencies

# Register your models here.
# admin.site.register(Countries)
# admin.site.register(Counties)
# admin.site.register(Constituencies)


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('country_abbr','country_code', 'country_name', 'date_created')
    list_filter = ('country_abbr','country_code', 'country_name', 'date_created')


@admin.register(Counties)
class CountiesAdmin(admin.ModelAdmin):
    list_display = ('county_code','county_name', 'country_id', 'date_created')
    list_filter = ('county_code','county_name', 'country_id', 'date_created')


@admin.register(Constituencies)
class ConstituenciesAdmin(admin.ModelAdmin):
    list_display = ('constituency_name','county_id', 'date_created')
    list_filter = ('constituency_name','county_id', 'date_created')

