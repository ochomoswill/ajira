from django.shortcuts import render
# Create your views here.
@admin.register(Recommendation)
class JobApplicantAdmin(admin.ModelAdmin):
    list_display = ('job_id','employer_id', 'worker_id', 'worker_phone_no', 'applicant_status','date_created')
    list_filter = ('job_id', 'employer_id', 'worker_id', 'applicant_status')