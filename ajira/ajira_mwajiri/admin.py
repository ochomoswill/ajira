from django.contrib import admin
from .models import Employer

# Register your models here.
#admin.site.register(Employer)


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('image_tag','employer_name', 'id_number', 'county_id', 'constituency_id', 'mobile_no','email_address', 'approval_status', 'date_created')
    list_filter = ('id_number', 'county_id', 'constituency_id', 'approval_status')

