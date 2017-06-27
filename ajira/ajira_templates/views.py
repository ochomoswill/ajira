
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import *
from ajira_parameters.models import Countries, Counties, Constituencies
from ajira_ajiriwa.models import Worker, Experience, WorkerNotification
from ajira_mwajiri.models import Employer
from ajira_jobs.models import Job,JobApplicant
from ajira_recommendations.models import Recommendation

import datetime

CURRENT_DATE = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
DEFAULT_APPROVAL_STATUS = "pending"
DEFAULT_EXPECTED_SALARY = 10000
DEFAULT_WORKER_BIO = "I am ..."
DEFAULT_PREFERRED_LOCATION = "Kitengela"





# Create your views here.



# ===========================================================================================================================
# Log In Page
# ===========================================================================================================================

def index(request):
    template = 'views/login.html'
    return render(request, template)



def login_view(request):
    email = request.POST.get('email_address')
    pwd = request.POST.get('pwd')

    user = auth.authenticate(username=email, password=pwd)

    if user is not None:
        if user.is_active:
            login(request, user)
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

            if (usertype == "ajiriwa"):
                current_user = Worker.objects.filter(email_address=email, user_password=pwd).values_list('worker_name', flat=True)[0]
                slug = Worker.objects.filter(email_address=email, user_password=pwd).values_list('slug', flat=True)[0]
                request.session['member_slug'] = slug
                request.session['member_usertype'] = usertype
            else:
                current_user = \
                    Employer.objects.filter(email_address=email, user_password=pwd).values_list('employer_name',flat=True)[0]
                slug = Employer.objects.filter(email_address=email, user_password=pwd).values_list('slug', flat=True)[0]
                request.session['member_slug'] = slug
                request.session['member_usertype'] = usertype

            print("Usertype:", usertype)
            print("Congratulations " + current_user + slug)
            message = "Congratulations " + str(current_user) + str(slug)
            return JsonResponse({"successful": message, "slug": slug, "usertype": usertype})


    else:
        print("Invalid Auth user credentials!")
        return JsonResponse({"errormsg": "Invalid user credentials!"})


def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    template = '/'
    return redirect(template)


# ===========================================================================================================================
# Home Page
# ===========================================================================================================================

def home(request):
    template = 'views/home/home.html'
    return render(request, template)


# ===========================================================================================================================
# Employer Page
# ===========================================================================================================================

def employer(request):
    template = 'views/employers/employers.html'
    return render(request, template)


def employer_reg(request):
    constituencies = Constituencies.objects.all()
    counties = Counties.objects.all()
    context = {'constituencies': constituencies, 'counties': counties}
    template = 'views/employers/client_registration.html'
    return render(request, template, context)


def register_mwajiri(request):
    email = request.POST.get('email_address')
    data = {
        'is_taken': Worker.objects.filter(email_address__iexact=email).exists()
    }
    if (Worker.objects.filter(email_address__iexact=email).exists()):
        return JsonResponse({"data": "The email already exists in the database!"})

    idnumber = request.POST.get('idNumber')
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    constituency = request.POST.get('constituency')
    county = request.POST.get('county')
    phoneNumber = request.POST.get('phoneNumber')

    # countyRecord = Counties.objects.filter(id=county).only("country_id")

    country = Counties.objects.filter(id=county).values_list('country_id', flat=True)[0]
    print(country)

    DEFAULT_SLUG = slugify(name)
    print(DEFAULT_SLUG)

    DEFAULT_AVATAR = "mwajiri_upload/2017/06/01/logo_sd3RGNe.png"

    query = "insert into ajira_mwajiri_employer" \
            "(employer_name,id_number,mobile_no,constituency_id_id,country_id_id,county_id_id,email_address,user_password, approval_status,employer_avatar, slug, date_created,date_modified)" \
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    conn = connection.cursor()

    conn.execute(query,
                 (name, idnumber, phoneNumber, constituency, country, county, email, pwd,
                  DEFAULT_APPROVAL_STATUS,
                  DEFAULT_AVATAR, DEFAULT_SLUG, CURRENT_DATE, CURRENT_DATE))

    # https://docs.djangoproject.com/en/1.8/topics/db/queries/
    # https: // simpleisbetterthancomplex.com / tutorial / 2016 / 11 / 22 / django - multiple - file - upload - using - ajax.html
    print(data)

    user = User.objects.create_user(email, email, pwd)

    ajiriwa_group = Group.objects.get(name='Mwajiri')
    ajiriwa_group.user_set.add(user)

    return JsonResponse({"data": "Successfully received!"})


def my_mwajiri_profile(request, slug):
    if not request.user.is_authenticated():
        return redirect('/require_employerloggedin')
    elif request.user.is_authenticated():
        employer = get_object_or_404(Employer, slug=slug)
        current_user_id = Employer.objects.filter(slug=slug).values_list('id', flat=True)[0]

        # Returns the total number of entries in the database.
        total_no_recommendations = Recommendation.objects.filter(employer_id= current_user_id).count()
        total_no_jobs = Job.objects.filter(employer_id= current_user_id).count()
        job_applicants = JobApplicant.objects.filter(employer_id=current_user_id)

        print(current_user_id)
        print (request.user)
        context = {'employer': employer, 'total_no_recommendations':total_no_recommendations, 'total_no_jobs':total_no_jobs, 'job_applicants':job_applicants}
        template = 'views/employers/my_account/my_mwajiri_profile.html'
        return render(request, template, context)

def edit_mwajiri_profile(request, slug):
    if not request.user.is_authenticated():
        return redirect('/require_loggedin')
    elif request.user.is_authenticated():
        employers = get_object_or_404(Employer, slug=slug)
        current_user_id = Employer.objects.filter(slug=slug, email_address=request.user).values_list('id', flat=True)[
            0]
        current_user_constituency_id = \
            Employer.objects.filter(slug=slug, email_address=request.user).values_list('constituency_id', flat=True)[
                0]
        current_user_county_id = \
            Employer.objects.filter(slug=slug, email_address=request.user).values_list('county_id', flat=True)[0]
        print("Current User ID: ", current_user_id)
        print ("Login User: ", request.user)
        print("Current Constituency ID: ", current_user_constituency_id)
        print ("Current County ID: ", current_user_county_id)
        constituency = Constituencies.objects.filter(id=current_user_constituency_id).values_list('id', flat=True)[
            0]
        print(constituency)
        county = Counties.objects.filter(id=current_user_county_id).values_list('id', flat=True)[0]
        # experiences = Experience.objects.filter(worker_id=current_user_id)
        # constituencies = Constituencies.objects.all()
        # counties = Counties.objects.all()
        context = {'employers': employers,"Wconstituency": constituency, "Wcounty": county}
        template = 'views/employers/my_account/edit_profile.html'
        return render(request, template, context)





# ===========================================================================================================================
# Worker Page
# ===========================================================================================================================
def ajiriwa_search_details(request):
    if request.method == 'POST':
        if request.POST.get('ajiriwa_name'):
            request.session['searchName'] = request.POST.get('ajiriwa_name')
        elif request.POST.get('skills') and request.POST.get('county') and request.POST.get('constituency'):
            request.session['searchSkill'] = request.POST.get('skills')
            request.session['searchCounty'] = request.POST.get('county')
            request.session['searchConstituency'] = request.POST.get('constituency')

        return JsonResponse({"data": "Ajiriwa search data successfully posted!"})

def ajiriwa_search_name(request):
    if request.method == 'POST':
        if request.POST.get('ajiriwa_name'):
            request.session['searchName'] = request.POST.get('ajiriwa_name')

        return JsonResponse({"data": "Ajiriwa search data successfully posted!"})

def ajiriwa(request):
    employees = Worker.objects.all().order_by('-date_created')
    paginator = Paginator(employees, 9)
    constituencies = Constituencies.objects.all()
    counties = Counties.objects.all()
    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)
    context = {"employees": employees ,'constituencies': constituencies, 'counties': counties, 'page': page}
    template = 'views/domestic_workers/domestic_workers.html'
    return render(request, template, context)

def ajiriwa_search(request):
    employees = Worker.objects.all()
    if request.session['searchSkill'] and request.session['searchCounty'] and request.session['searchConstituency']:
        employees = Worker.objects.filter(skills=request.session['searchSkill'], county_id=request.session['searchCounty'], constituency_id=request.session['searchConstituency'])

    # elif request.session['searchSkill']:
    #     pass
    # elif request.session['searchCounty']:
    #     pass
    # elif request.session['searchConstituency']:
    #     pass
    paginator = Paginator(employees, 9)
    constituencies = Constituencies.objects.all()
    counties = Counties.objects.all()
    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)
    context = {"employees": employees ,'constituencies': constituencies, 'counties': counties, 'page': page}
    template = 'views/domestic_workers/domestic_workers.html'

    # if request.session['searchName']:
    #     del request.session['searchName']
    # elif request.session['searchSkill'] and request.session['searchCounty'] and request.session['searchConstituency']:
    #     del request.session['searchSkill']
    #     del request.session['searchCounty']
    #     del request.session['searchConstituency']


    return render(request, template, context)

def search_ajiriwa_by_name(request):
    employees = Worker.objects.all()
    if request.session['searchName']:
        employees = Worker.objects.filter(worker_name__icontains=request.session['searchName'])
    paginator = Paginator(employees, 9)
    constituencies = Constituencies.objects.all()
    counties = Counties.objects.all()
    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)
    context = {"employees": employees ,'constituencies': constituencies, 'counties': counties, 'page': page}
    template = 'views/domestic_workers/domestic_workers.html'

    return render(request, template, context)


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
    if (Worker.objects.filter(email_address__iexact=email).exists()):
        return JsonResponse({"data": "The email already exists in the database!"})

    idnumber = request.POST.get('idNumber')
    name = request.POST.get('name')
    birthDate = request.POST.get('birthDate')
    pwd = request.POST.get('pwd')
    constituency = request.POST.get('constituency')
    county = request.POST.get('county')
    skills = request.POST.get('skills')
    phoneNumber = request.POST.get('phoneNumber')

    # countyRecord = Counties.objects.filter(id=county).only("country_id")

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
                 (name, idnumber, skills, birthDate, phoneNumber, constituency, country, county, email, pwd,
                  DEFAULT_WORKER_BIO, DEFAULT_EXPECTED_SALARY, DEFAULT_PREFERRED_LOCATION, DEFAULT_APPROVAL_STATUS,
                  DEFAULT_AVATAR, DEFAULT_SLUG, CURRENT_DATE, CURRENT_DATE))

    # https://docs.djangoproject.com/en/1.8/topics/db/queries/
    # https: // simpleisbetterthancomplex.com / tutorial / 2016 / 11 / 22 / django - multiple - file - upload - using - ajax.html
    print(data)

    user = User.objects.create_user(email, email, pwd)

    ajiriwa_group = Group.objects.get(name='Ajiriwa')
    ajiriwa_group.user_set.add(user)

    return JsonResponse({"data": "Successfully received!"})


# @login_required
def ajiriwa_profile(request, slug):
    if not request.user.is_authenticated():
        return redirect('/require_loggedin')
    elif request.user.is_authenticated():
        employees = get_object_or_404(Worker, slug=slug)
        current_user_id = Worker.objects.filter(slug=slug).values_list('id', flat=True)[0]
        print(current_user_id)
        print (request.user)
        experiences = Experience.objects.filter(worker_id=current_user_id)
        recommendations = Recommendation.objects.filter(worker_id=current_user_id)
        context = {'employees': employees, "experiences": experiences, "recommendations": recommendations}
        template = 'views/domestic_workers/ajiriwa_profile.html'
        return render(request, template, context)




def my_profile(request, slug):
    if not request.user.is_authenticated():
        return redirect('/require_loggedin')
    elif request.user.is_authenticated():
        employees = get_object_or_404(Worker, slug=slug)
        current_user_id = Worker.objects.filter(slug=slug).values_list('id', flat=True)[0]
        print(current_user_id)
        print (request.user)
        notifications = WorkerNotification.objects.filter(worker_id=current_user_id).order_by('-date_created')
        experiences = Experience.objects.filter(worker_id=current_user_id)
        recommendations = Recommendation.objects.filter(worker_id=current_user_id)
        context = {'employees': employees, "experiences": experiences, "recommendations": recommendations, "notifications":notifications}

        template = 'views/my_account/my_profile.html'
        return render(request, template, context)


def edit_profile(request, slug):
    if not request.user.is_authenticated():
        return redirect('/require_loggedin')
    elif request.user.is_authenticated():
        employees = get_object_or_404(Worker, slug=slug)
        current_user_id = Worker.objects.filter(slug=slug, email_address=request.user).values_list('id', flat=True)[0]
        current_user_constituency_id = \
            Worker.objects.filter(slug=slug, email_address=request.user).values_list('constituency_id', flat=True)[0]
        current_user_county_id = \
            Worker.objects.filter(slug=slug, email_address=request.user).values_list('county_id', flat=True)[0]
        print("Current User ID: ", current_user_id)
        print ("Login User: ", request.user)
        print("Current Constituency ID: ", current_user_constituency_id)
        print ("Current County ID: ", current_user_county_id)
        constituency = Constituencies.objects.filter(id=current_user_constituency_id).values_list('id', flat=True)[0]
        print(constituency)
        county = Counties.objects.filter(id=current_user_county_id).values_list('id', flat=True)[0]
        notifications = WorkerNotification.objects.filter(worker_id=current_user_id).order_by('-date_created')
        experiences = Experience.objects.filter(worker_id=current_user_id)
        constituencies = Constituencies.objects.all()
        counties = Counties.objects.all()
        context = {'employees': employees, "experiences": experiences, 'constituencies': constituencies,
                   'counties': counties, "Wconstituency": constituency, "Wcounty": county, "notifications":notifications}
        template = 'views/domestic_workers/edit_profile.html'
        return render(request, template, context)


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        if request.session["member_usertype"] == "ajiriwa":
            # current_user_id = Worker.objects.filter(email_address=request.user).values_list('id', flat=True)[0]
            if request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                print(uploaded_file_url)
                Worker.objects.filter(email_address=request.user).update(worker_avatar=uploaded_file_url)
                return redirect('/edit_profile/' + request.session['member_slug'] + '/',
                                {'uploaded_file_url': uploaded_file_url})
        elif request.session["member_usertype"] == "mwajiri":
            # current_user_id = Employer.objects.filter(email_address=request.user).values_list('id', flat=True)[0]
            if request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                print(uploaded_file_url)
                Employer.objects.filter(email_address=request.user).update(employer_avatar=uploaded_file_url)
                return redirect('/edit_mwajiri_profile/' + request.session['member_slug'] + '/',
                                {'uploaded_file_url': uploaded_file_url})
    return redirect('/edit_mwajiri_profile/' + request.session['member_slug'] + '/')


def update_profile_details(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        about = request.POST.get('about')
        constituency = request.POST.get('constituency')
        county = request.POST.get('county')
        skills = request.POST.get('skills')
        phoneNumber = request.POST.get('phoneNumber')
        preferredLocation = request.POST.get('preferredLocation')
        expectedSalary = request.POST.get('expectedSalary')
        Worker.objects.filter(email_address=request.user).update(worker_name=fullname,
                                                                 worker_bio=about,
                                                                 constituency_id=constituency,
                                                                 county_id=county,
                                                                 skills=skills,
                                                                 mobile_no=phoneNumber,
                                                                 preferred_locations=preferredLocation,
                                                                 expected_salary=expectedSalary)
        return JsonResponse({"data": "Profile Successfully Updated!"})


def add_experience(request):
    if request.method == 'POST':
        jobTitle = request.POST.get('jobTitle')
        company = request.POST.get('company')
        location = request.POST.get('location')
        fromDate = request.POST.get('fromDate')
        toDate = request.POST.get('toDate')
        jobDescription = request.POST.get('jobDescription')
        worker = Worker.objects.filter(email_address=request.user)
        current_user_id = Worker.objects.filter(email_address=request.user).values_list('id', flat=True)[0]

        # p = Experience(worker_id=worker,
        #                job_title=jobTitle,
        #                job_description=jobDescription,
        #                company=company,
        #                job_location=location,
        #                from_date=fromDate,
        #                to_date=toDate,
        #                approval_status=DEFAULT_APPROVAL_STATUS,
        #                date_created=CURRENT_DATE,
        #                date_modified=CURRENT_DATE)

        query = "insert into ajira_ajiriwa_experience (worker_id_id,job_title,job_description,company,job_location,from_date,to_date,approval_status,date_created,date_modified)\
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        conn = connection.cursor()

        conn.execute(query, (
            current_user_id, jobTitle, jobDescription, company, location, fromDate, toDate, DEFAULT_APPROVAL_STATUS,
            CURRENT_DATE, CURRENT_DATE))

        # (worker, jobTitle, jobDescription, company,location, fromDate, toDate, DEFAULT_APPROVAL_STATUS, CURRENT_DATE, CURRENT_DATE)
        # p.save()
        return JsonResponse({"data": "Profile Successfully Updated!"})


# ===========================================================================================================================
# Job Page
# ===========================================================================================================================
def job_search_details(request):
    if request.method == 'POST':
        request.session['searchJob'] = request.POST.get('jobs')
        request.session['searchJobCounty'] = request.POST.get('county')
        request.session['searchJobConstituency'] = request.POST.get('constituency')
        return JsonResponse({"data": "Jobs search data successfully posted!"})

def post_job(request):
    if not request.user.is_authenticated():
        return redirect('/require_employerloggedin')
    elif request.session["member_usertype"] == "ajiriwa":
        return redirect('/require_employerloggedin')
    elif request.user.is_authenticated() and request.session["member_usertype"] == "mwajiri":
        constituencies = Constituencies.objects.all()
        counties = Counties.objects.all()
        context = {'constituencies': constituencies, 'counties': counties}
        template = 'views/jobs/post_job.html'
        return render(request, template, context)


def post_job_details(request):
    if request.method == 'POST':
        jobTitle = request.POST.get('jobTitle')
        jobDescription = request.POST.get('jobDescription')
        constituency = request.POST.get('constituency')
        county = request.POST.get('county')

        current_user_id = Employer.objects.filter(email_address=request.user).values_list('id', flat=True)[0]

        jobSlug = slugify(jobTitle + str(county) + str(constituency) + str(CURRENT_DATE))

        query = "insert into ajira_jobs_job (employer_id_id, job_title,job_description,approval_status,job_status,constituency_id_id,county_id_id,slug, date_created,date_modified)\
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        conn = connection.cursor()

        DEFAULT_JOB_STATUS = "VACANT"
        conn.execute(query, (
            current_user_id, jobTitle, jobDescription, DEFAULT_APPROVAL_STATUS, DEFAULT_JOB_STATUS, constituency,
            county,jobSlug, CURRENT_DATE, CURRENT_DATE))

        return JsonResponse({"data": "Job was successfully posted!"})


def view_job(request):
    if not request.user.is_authenticated():
        return redirect('/require_loggedin')
    elif request.user.is_authenticated():
        slug = request.session['member_slug']
        current_user_id = Worker.objects.filter(slug=slug).values_list('id', flat=True)[0]
        notifications = WorkerNotification.objects.filter(worker_id=current_user_id).order_by('-date_created')
        jobs = Job.objects.all()
        constituencies = Constituencies.objects.all()
        counties = Counties.objects.all()
        paginator = Paginator(jobs, 9)
        page = request.GET.get('page')
        try:
            jobs = paginator.page(page)
        except PageNotAnInteger:
            jobs = paginator.page(1)
        except EmptyPage:
            jobs = paginator.page(paginator.num_pages)
        context = {"jobs":jobs, 'page': page,'constituencies': constituencies, 'counties': counties, 'notifications':notifications}
        template = 'views/jobs/view_job.html'
        return render(request, template, context)

def job_search(request):
    jobs = Job.objects.all()
    if request.session['searchJob'] and request.session['searchJobCounty'] and request.session['searchJobConstituency']:
        jobs = Job.objects.filter(job_title=request.session['searchJob'], county_id=request.session['searchJobCounty'], constituency_id=request.session['searchJobConstituency'])
    # elif request.session['searchSkill']:
    #     pass
    # elif request.session['searchCounty']:
    #     pass
    # elif request.session['searchConstituency']:
    #     pass
    paginator = Paginator(jobs, 9)
    constituencies = Constituencies.objects.all()
    counties = Counties.objects.all()
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    context = {"jobs": jobs ,'constituencies': constituencies, 'counties': counties, 'page': page}
    template = 'views/jobs/view_job.html'
    return render(request, template, context)

def single_job(request, slug):
    if not request.user.is_authenticated():
        return redirect('/require_loggedin')
    elif request.user.is_authenticated():
        if request.session['member_slug']:
            user_slug = request.session['member_slug']
            workers = Worker.objects.filter(slug=user_slug)
            current_user_id = Worker.objects.filter(slug=user_slug).values_list('id', flat=True)[0]
            notifications = WorkerNotification.objects.filter(worker_id=current_user_id).order_by('-date_created')
            job = get_object_or_404(Job, slug=slug)
            context = {"job": job, "workers":workers, "notifications":notifications}
            template = 'views/jobs/job_profile.html'
            return render(request, template, context)
        job = get_object_or_404(Job, slug=slug)
        context = {"job" : job}
        template = 'views/jobs/job_profile.html'
        return render(request, template, context)

def applicant_details(request):
    if request.method == 'POST':
        applicant_email = request.POST.get('applicantEmail')
        applicant_phoneno = request.POST.get('applicantPhoneNo')
        job_id = request.POST.get('jobId')
        print("Job id: ", job_id)
        worker_id = Worker.objects.filter(email_address=applicant_email).values_list('id', flat=True)[0]
        employer_id = Job.objects.filter(id=job_id).values_list('employer_id', flat=True)[0]
        print("Employer id: ", employer_id)

        # query = "insert into ajira_jobs_job (employer_id_id, job_title,job_description,approval_status,job_status,constituency_id_id,county_id_id,slug, date_created,date_modified)\
        #         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        query = "INSERT INTO ajira_jobs_jobapplicant(worker_phone_no, applicant_status, date_created, employer_id_id,job_id_id, worker_id_id)\
        VALUES(%s, %s, %s, %s, %s, %s)"

        conn = connection.cursor()
        conn.execute(query, (applicant_phoneno, DEFAULT_APPROVAL_STATUS, CURRENT_DATE, employer_id, job_id, worker_id))

        applicant_message = "Your job application was successful. Await information from the employer"

        message = notify(worker_id, applicant_message, "System Notification", "UNREAD", CURRENT_DATE, CURRENT_DATE)

        return JsonResponse({"data": "Applicant data successfully posted!"})



# ===========================================================================================================================
# Recommendations Page
# ===========================================================================================================================
def recommendee_details(request):
    if request.method == 'POST':
        recommendee_email = request.POST.get('recommendeeEmail')
        request.session['recommendee_email'] = recommendee_email
        return JsonResponse({"data": "Recommendee data successfully posted!"})


def recommend(request):
    if not request.user.is_authenticated():
        return redirect('/require_employerloggedin')
    elif request.session["member_usertype"] == "ajiriwa":
        return redirect('/require_employerloggedin')
    elif request.user.is_authenticated() and request.session["member_usertype"] == "mwajiri":
        if request.session['recommendee_email']:
            recommendee_email = request.session['recommendee_email']
            workers = Worker.objects.filter(email_address=recommendee_email)
            current_recommendee_id = Worker.objects.filter(email_address=recommendee_email).values_list('id', flat=True)[0]
            request.session['current_recommendee_id'] = current_recommendee_id
            experiences = Experience.objects.filter(worker_id=current_recommendee_id)
            template = 'views/recommendations/give_recommendations.html'
            context = {'workers': workers, "experiences":experiences}
            return render(request,template,context)
        workers = Worker.objects.all()
        template = 'views/recommendations/give_recommendations.html'
        context = {'workers': workers}
        return render(request, template, context)


def make_recommendation(request):
    if request.method == 'POST':
        jobTitle = request.POST.get('jobTitle')
        relationship = request.POST.get('relationship')
        recommendee = request.session['current_recommendee_id']
        remark = request.POST.get('remark')
        tag = request.POST.get('tag')

        current_user_id = Employer.objects.filter(email_address=request.user).values_list('id', flat=True)[0]
        current_user_name = Employer.objects.filter(email_address=request.user).values_list('employer_name', flat=True)[0]

        query = "insert into ajira_recommendations_recommendation (employer_id_id, worker_id_id,tag, relationship, position_or_skills_at_that_time,remark, date_created,date_modified)\
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

        conn = connection.cursor()

        conn.execute(query, (
            current_user_id, recommendee, tag, relationship, jobTitle, remark, CURRENT_DATE, CURRENT_DATE))

        recommendee_message = current_user_name + " " + "has recommended you!"

        message = notify(recommendee, recommendee_message, "System Notification", "UNREAD", CURRENT_DATE, CURRENT_DATE)

        return JsonResponse({"data": message})


# ===========================================================================================================================
# Notifications Page
# ===========================================================================================================================
def my_notifications(request, slug):
    if not request.user.is_authenticated():
        return redirect('/require_loggedin')
    elif request.user.is_authenticated():
        if request.session["member_usertype"] == "ajiriwa":
            employees = get_object_or_404(Worker, slug=slug)
            current_user_id = Worker.objects.filter(slug=slug).values_list('id', flat=True)[0]
            print(current_user_id)
            print (request.user)
            notifications = WorkerNotification.objects.filter(worker_id=current_user_id).order_by('-date_created')
            context = {'employees': employees, "notifications":notifications}
        elif request.session["member_usertype"] == "mwajiri":
            employers = get_object_or_404(Employer, slug=slug)
            current_user_id = Employer.objects.filter(slug=slug).values_list('id', flat=True)[0]

            print(current_user_id)
            print (request.user)
            context = {'employers': employers}
        template = 'views/my_account/my_notification.html'
        return render(request, template, context)


# ===========================================================================================================================
# Error Page
# ===========================================================================================================================

def pagenot_found(request):
    template = 'views/error_pages/404.html'
    return render(request, template)

def require_loggedin(request):
    template = 'views/error_pages/need_to_login.html'
    return render(request, template)

def require_employerloggedin(request):
    template = 'views/error_pages/need_employer_login.html'
    return render(request, template)

# ===========================================================================================================================
# Utilities Page
# ===========================================================================================================================

def notify(worker_id, message, sender, message_status, date_created, date_received):
    query = "INSERT INTO ajira_ajiriwa_workernotification (message, sender, message_status, date_created, date_received, worker_id_id) VALUES (%s, %s, %s, %s, %s, %s)"

    conn = connection.cursor()

    if conn.execute(query, (message, sender, message_status, date_created, date_received,worker_id)):
        return "Notification was successful sent!"

    return "Notification wasn't successful sent!"

