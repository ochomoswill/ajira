from django.db import models
from django.utils import timezone
from ajira_mwajiri.models import Employer


# Create your models here.

APPROVAL_STATUS = (('approved', 'APPROVED'), ('pending', 'PENDING'),('declined', 'DECLINED'),)
JOB_STATUS = (('vacant', 'VACANT'), ('filled', 'FILLED'),)


class Job(models.Model):
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    approval_status = models.CharField(max_length=20, choices=APPROVAL_STATUS, default='pending')
    job_status = models.CharField(max_length=20, choices=JOB_STATUS, default='vacant')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job_title
