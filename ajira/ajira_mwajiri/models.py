from django.db import models
from django.utils import timezone
from ajira_parameters.models import Countries, Counties, Constituencies
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe



# Create your models here.

APPROVAL_STATUS = (('approved', 'APPROVED'), ('pending', 'PENDING'),('declined', 'DECLINED'),)


class Employer(models.Model):
    employer_name = models.CharField(max_length=50)
    id_number = models.IntegerField()
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)
    county_id = models.ForeignKey(Counties, on_delete=models.CASCADE)
    constituency_id = models.ForeignKey(Constituencies, on_delete=models.CASCADE)
    mobile_no = models.IntegerField()
    email_address = models.CharField(max_length=50, default="123@hotmail.com")
    user_password = models.CharField(max_length=50, default="1234")
    approval_status = models.CharField(max_length=20, choices=APPROVAL_STATUS, default='pending')

    employer_avatar = models.ImageField(upload_to='mwajiri_upload/%Y/%m/%d/',
                                      default='mwajiri_upload/2017/06/01/logo_sd3RGNe.png')
    slug = models.SlugField(max_length=250,default="dog-poo")

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)

    # creates the slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.employer_name)
        super(Employer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ajiriwa_profile', args=[self.slug])

    def image_tag(self):
        string = str(self.employer_avatar)
        first_string = string.split('/')
        print(first_string[1])
        if first_string[1] == "ajira_media":
            return mark_safe('<img src="%s" width="150" height="150" />' % (self.employer_avatar))
        return mark_safe('<img src="/ajira_media/%s" width="150" height="150" />' % (self.employer_avatar))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.employer_name



