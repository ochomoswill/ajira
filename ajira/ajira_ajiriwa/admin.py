from django.contrib import admin
from .models import Worker, Experience

# Register your models here.



@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('image_tag','worker_name', 'id_number', 'county_id', 'constituency_id', 'skills', 'mobile_no','email_address', 'approval_status', 'date_created')
    list_filter = ('id_number', 'county_id', 'constituency_id', 'approval_status')

    # fields = ('image_tag',)
    # readonly_fields = ('image_tag',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('worker_id', 'job_title', 'job_location', 'from_date', 'to_date', 'approval_status','date_created')
    list_filter = ('worker_id', 'job_title', 'job_location', 'approval_status')
