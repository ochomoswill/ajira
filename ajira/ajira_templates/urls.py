"""aura_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from . import views
#setting up the media
from django.conf.urls.static import static

urlpatterns = [
    # Login page
    url(r'^index/$', views.index, name='index'),
    url(r'^login_view/$', views.login_view, name='login_view'),
    url(r'^logout_view/$', views.logout_view, name='logout_view'),
    # Home page
    url(r'^$', views.home, name='home'),
    # Employer page
    url(r'^employer/$', views.employer, name='employer'),
    url(r'^employer_reg/$', views.employer_reg, name='employer_reg'),
    url(r'^register_mwajiri/$', views.register_mwajiri, name='register_mwajiri'),
    url(r'^my_mwajiri_profile/(?P<slug>[-\w]+)/$', views.my_mwajiri_profile, name='my_mwajiri_profile'),
    url(r'^edit_mwajiri_profile/(?P<slug>[-\w]+)/$', views.edit_mwajiri_profile, name='edit_mwajiri_profile'),
    # Worker page
    url(r'^ajiriwa/$', views.ajiriwa, name='ajiriwa'),
    url(r'^ajiriwa_reg/$', views.ajiriwa_reg, name='ajiriwa_reg'),
    url(r'^register_ajiriwa/$', views.register_ajiriwa, name='register_ajiriwa'),
    url(r'^edit_profile/(?P<slug>[-\w]+)/$', views.edit_profile, name='edit_profile'),
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    url(r'^update_profile_details/$', views.update_profile_details, name='update_profile_details'),
    url(r'^add_experience/$', views.add_experience, name='add_experience'),
    url(r'^ajiriwa_profile/(?P<slug>[-\w]+)/$', views.ajiriwa_profile, name='ajiriwa_profile'),
    url(r'^my_profile/(?P<slug>[-\w]+)/$', views.my_profile, name='my_profile'),
    url(r'^my_notifications/(?P<slug>[-\w]+)/$', views.my_notifications, name='my_notifications'),

    # Job Page
    url(r'^post_job/$', views.post_job, name='post_job'),
    url(r'^post_job_details/$', views.post_job_details, name='post_job_details'),
    url(r'^view_job/$', views.view_job, name='view_job'),
    url(r'^view_job_profile/(?P<slug>[-\w]+)/$', views.single_job, name='view_job_profile'),
    # Recommendations Page
    url(r'^recommend/$', views.recommend, name='recommend'),
    url(r'^recommendee_details/$', views.recommendee_details, name='recommendee_details'),
    url(r'^make_recommendation/$', views.make_recommendation, name='make_recommendation'),
    # Error Page
    url(r'^page_not_found/$', views.pagenot_found, name='page_not_found'),
    url(r'^require_loggedin/$', views.require_loggedin, name='require_loggedin'),
    url(r'^require_employerloggedin/$', views.require_employerloggedin, name='require_employerloggedin'),


]




#setting up the media file
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)