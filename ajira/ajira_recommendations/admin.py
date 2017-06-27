from django.contrib import admin
from .models import Recommendation

# Register your models here.
#admin.site.register(Recommendation)


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('employer_id','worker_id', 'position_or_skills_at_that_time', 'date_created')
    list_filter = ('employer_id','worker_id', 'position_or_skills_at_that_time')
