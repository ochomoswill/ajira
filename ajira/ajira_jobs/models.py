from django.db import models
from django.utils import timezone
from ajira_mwajiri.models import Employer
from ajira_ajiriwa.models import Worker
from ajira_parameters.models import Countries, Counties, Constituencies
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


# Create your models here.

APPROVAL_STATUS = (('approved', 'APPROVED'), ('pending', 'PENDING'),('declined', 'DECLINED'),)
JOB_STATUS = (('vacant', 'VACANT'), ('filled', 'FILLED'),)


class Job(models.Model):
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    county_id = models.ForeignKey(Counties, on_delete=models.CASCADE, default=1)
    constituency_id = models.ForeignKey(Constituencies, on_delete=models.CASCADE, default=1)
    approval_status = models.CharField(max_length=20, choices=APPROVAL_STATUS, default='pending')
    job_status = models.CharField(max_length=20, choices=JOB_STATUS, default='vacant')
    slug = models.SlugField(max_length=250, default="dog-poo")

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)

    # creates the slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.job_title + str(self.county_id) + str(self.constituency_id) + str(self.date_created))
        super(Job, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_job_profile', args=[self.slug])

    def __str__(self):
        return self.job_title


class JobApplicant(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    worker_phone_no = models.IntegerField()

    applicant_status = models.CharField(max_length=20, choices=APPROVAL_STATUS, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant_status
