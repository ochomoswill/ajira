from django.db import models
from django.utils import timezone
from ajira_parameters.models import Countries, Counties, Constituencies



# Create your models here.

APPROVAL_STATUS = (('approved', 'APPROVED'), ('pending', 'PENDING'),('declined', 'DECLINED'),)


class Employer(models.Model):
    employer_name = models.CharField(max_length=50)
    id_number = models.IntegerField()
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)
    county_id = models.ForeignKey(Counties, on_delete=models.CASCADE)
    constituency_id = models.ForeignKey(Constituencies, on_delete=models.CASCADE)
    mobile_no = models.IntegerField()
    email_address = models.CharField(max_length=50, default="123@example.com")
    user_password = models.CharField(max_length=50, default="1234")
    approval_status = models.CharField(max_length=20, choices=APPROVAL_STATUS, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.employer_name



