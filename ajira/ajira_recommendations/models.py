from django.db import models
from django.utils import timezone
from ajira_mwajiri.models import Employer
from ajira_ajiriwa.models import Worker


# Create your models here.


class Recommendation(models.Model):
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    relationship = models.TextField()
    position_or_skills_at_that_time = models.TextField()
    remark = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tag
