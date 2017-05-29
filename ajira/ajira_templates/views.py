from django.core.files.base import ContentFile
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.shortcuts import *
from ajira_parameters.models import Countries, Counties, Constituencies
from ajira_ajiriwa.models import Worker, Experience
from ajira_mwajiri.models import Employer

import datetime


CURRENT_DATE = datetime.datetime.now().strftime ("%Y-%m-%d")
DEFAULT_APPROVAL_STATUS = "pending"
DEFAULT_EXPECTED_SALARY = 10000
DEFAULT_WORKER_BIO = "I am ..."
DEFAULT_PREFERRED_LOCATION = "Kitengela"

# from django.core.files.uploadedfile import InMemoryUploadedFile
# from PIL import Image
# import StringIO
#
# def MakeThumbnail(file):
#     img = Image.open(file)
#     img.thumbnail((128, 128), Image.ANTIALIAS)
#     thumbnailString = StringIO.StringIO()
#     img.save(thumbnailString, 'PNG')
#     newFile = ContentFile(thumbnailString)
#     return newFile

# Create your views here.

# ===========================================================================================================================
# Log In Page
# ===========================================================================================================================

def index(request):
    template = 'views/login.html'
    return render(request,template)

def login(request):
    email = request.POST.get('email_address')
    pwd = request.POST.get('pwd')

    try:
        current_user = Worker.objects.get(email_address=email, user_password=pwd)
        usertype = "ajiriwa"
    except Worker.DoesNotExist:
        try:
            current_user = Employer.objects.get(email_address=email, user_password=pwd)
            usertype = "mwajiri"
        except Employer.DoesNotExist:
            current_user = False
            print("Invalid user credentials!")
            return JsonResponse({"errormsg": "Invalid user credentials!"})

    print(current_user)

    if(usertype == "ajiriwa"):
        current_user = Worker.objects.filter(email_address=email, user_password=pwd).values_list('worker_name', flat=True)[0]
        slug = Worker.objects.filter(email_address=email, user_password=pwd).values_list('slug', flat=True)[0]
    else:
        current_user = Employer.objects.filter(email_address=email, user_password=pwd).values_list('employee_name', flat=True)[0]


    print("Congratulations " + current_user + slug)
    message = "Congratulations " + str(current_user) + str(slug)
    return JsonResponse({"successful": message, "slug": slug})




# ===========================================================================================================================
# Home Page
# ===========================================================================================================================

def home(request):
    template = 'views/home/home.html'
    return render(request,template)

# ===========================================================================================================================
# Employer Page
# ===========================================================================================================================

def employer(request):
    template = 'views/employers/employers.html'
    return render(request,template)

def employer_reg(request):
    constituencies = Constituencies.objects.all()
    counties = Counties.objects.all()
    context = {'constituencies': constituencies, 'counties': counties}
    template = 'views/employers/client_registration.html'
    return render(request,template, context)


# ===========================================================================================================================
# Worker Page
# ===========================================================================================================================

def ajiriwa(request):
    employees = Worker.objects.all()
    context = {"employees": employees}
    template = 'views/domestic_workers/domestic_workers.html'
    return render(request,template, context)

def ajiriwa_reg(request):
    constituencies = Constituencies.objects.all()
    counties = Counties.objects.all()
    context = {'constituencies': constituencies, 'counties': counties}
    template = 'views/domestic_workers/employee_registration.html'
    return render(request, template, context)


def register_ajiriwa(request):
    email = request.POST.get('email_address')
    data = {
        'is_taken': Worker.objects.filter(email_address__iexact=email).exists()
    }
    if(Worker.objects.filter(email_address__iexact=email).exists()):
        return JsonResponse({"data":"The email already exists in the database!"})

    idnumber = request.POST.get('idNumber')
    name = request.POST.get('name')
    birthDate = request.POST.get('birthDate')
    pwd = request.POST.get('pwd')
    constituency = request.POST.get('constituency')
    county = request.POST.get('county')
    skills = request.POST.get('skills')
    phoneNumber = request.POST.get('phoneNumber')


    #countyRecord = Counties.objects.filter(id=county).only("country_id")

    country = Counties.objects.filter(id=county).values_list('country_id', flat=True)[0]
    print(country)

    DEFAULT_SLUG = slugify(name)
    print(DEFAULT_SLUG)

    DEFAULT_AVATAR = "ajiriwa_upload/2017/05/24/male.jpg"



    query = "insert into ajira_ajiriwa_worker" \
            "(worker_name,id_number,skills,birth_year,mobile_no,constituency_id_id,country_id_id,county_id_id,email_address,user_password,worker_bio, expected_salary,preferred_locations, approval_status,worker_avatar, slug, date_created,date_modified)" \
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s)"

    conn = connection.cursor()

    conn.execute(query,
                 (name,idnumber, skills,birthDate,phoneNumber,constituency,country,county, email,pwd,DEFAULT_WORKER_BIO,DEFAULT_EXPECTED_SALARY,DEFAULT_PREFERRED_LOCATION,DEFAULT_APPROVAL_STATUS ,DEFAULT_AVATAR,DEFAULT_SLUG,CURRENT_DATE,CURRENT_DATE))

    #https://docs.djangoproject.com/en/1.8/topics/db/queries/
    #https: // simpleisbetterthancomplex.com / tutorial / 2016 / 11 / 22 / django - multiple - file - upload - using - ajax.html
    print(data)
    return JsonResponse({"data":"Successfully received!"})

def ajiriwa_profile(request, slug):
    employees = get_object_or_404(Worker, slug=slug)
    current_user_id = Worker.objects.filter(slug=slug).values_list('id', flat=True)[0]
    print(current_user_id)
    experiences = Experience.objects.filter(worker_id=current_user_id)
    context = {'employees': employees, "experiences":experiences}
    template = 'views/my_account/my_profile.html'
    return render(request, template, context)

def edit_profile(request):
    template = 'views/domestic_workers/edit_profile.html'
    return render(request,template)



def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        return render(request, 'views/domestic_workers/edit_profile.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'views/domestic_workers/edit_profile.html')


# ===========================================================================================================================
# Job Page
# ===========================================================================================================================
def post_job(request):
    constituencies = Constituencies.objects.all()
    counties = Counties.objects.all()
    context = {'constituencies': constituencies, 'counties': counties}
    template = 'views/jobs/post_job.html'
    return render(request,template,context)

def view_job(request):
    template = 'views/jobs/view_job.html'
    return render(request, template)


# ===========================================================================================================================
# Recommendations Page
# ===========================================================================================================================
def recommend(request):
    template = 'views/recommendations/give_recommendations.html'
    return render(request,template)



