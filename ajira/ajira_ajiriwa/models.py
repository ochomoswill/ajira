from django.db import models
from django.utils import timezone
from ajira_parameters.models import Countries, Counties, Constituencies
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


# Create your models here.

APPROVAL_STATUS = (('approved', 'APPROVED'), ('pending', 'PENDING'),('declined', 'DECLINED'),)


class Worker(models.Model):
    worker_name = models.CharField(max_length=50)
    id_number = models.IntegerField()
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)
    county_id = models.ForeignKey(Counties, on_delete=models.CASCADE)
    constituency_id = models.ForeignKey(Constituencies, on_delete=models.CASCADE)
    skills = models.TextField()
    birth_year = models.DateField(default=timezone.now)
    mobile_no = models.IntegerField()
    email_address = models.EmailField(default="123@example.com")
    user_password = models.CharField(max_length=50, default="1234")
    worker_bio = models.TextField(default="I am ...", null=True, blank=True)
    preferred_locations = models.CharField(default="Kitengela", max_length=100, null=True, blank=True)
    expected_salary = models.DecimalField(default="10000", decimal_places=2, max_digits=10, null=True, blank=True)
    approval_status = models.CharField(max_length=20, choices=APPROVAL_STATUS, default='pending')

    worker_avatar = models.ImageField(upload_to='ajiriwa_upload/%Y/%m/%d/', default='ajiriwa_upload/2017/05/24/male.jpg')
    slug = models.SlugField(max_length=250, default="dog-poo")

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)

    # creates the slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.worker_name)
        super(Worker, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ajiriwa_profile', args=[self.slug])

    def __str__(self):
        return self.worker_name


class Experience(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    approval_status = models.CharField(max_length=20, choices=APPROVAL_STATUS, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job_title

