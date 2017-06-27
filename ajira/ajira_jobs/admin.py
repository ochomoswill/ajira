from django.contrib import admin
from .models import Job, JobApplicant

# Register your models here.
# admin.site.register(Job)
#
# admin.site.register(JobApplicant)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('employer_id','job_title','county_id', 'constituency_id','approval_status', 'date_created')
    list_filter = ('employer_id','job_title', 'county_id', 'constituency_id', 'approval_status')

@admin.register(JobApplicant)
class JobApplicantAdmin(admin.ModelAdmin):
    list_display = ('job_id','employer_id', 'worker_id', 'worker_phone_no', 'applicant_status','date_created')
    list_filter = ('job_id', 'employer_id', 'worker_id', 'applicant_status')