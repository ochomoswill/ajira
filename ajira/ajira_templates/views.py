from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ajira_parameters.models import Countries, Counties, Constituencies
from ajira_ajiriwa.models import Worker

# Create your views here.

# ===========================================================================================================================
# Log In Page
# ===========================================================================================================================

def index(request):
    template = 'views/login.html'
    return render(request,template)

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
    template = 'views/employers/client_registration.html'
    return render(request,template)


# ===========================================================================================================================
# Worker Page
# ===========================================================================================================================

def ajiriwa(request):
    template = 'views/domestic_workers/domestic_workers.html'
    return render(request,template)

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

    name = request.POST.get('name')
    birthDate = request.POST.get('birthDate')
    pwd = request.POST.get('pwd')
    constituency = request.POST.get('constituency')
    county = request.POST.get('county')
    skills = request.POST.get('skills')
    phoneNumber = request.POST.get('phoneNumber')

    formInstance = Worker(email_address=email,
                                      worker_name=name,
                                      birth_year=birthDate,
                                      user_password=pwd,
                                      constituency_id=constituency,
                                      county_id=county,
                                      skills=skills,
                                      mobile_no=phoneNumber
                                      )
    formInstance.save()


    #https://docs.djangoproject.com/en/1.8/topics/db/queries/

    print(data)
    return JsonResponse({"data":"Successfully received!"})

# def populate_constituencies(request):
#     constituencies = Constituencies.objects.all()
#     context = {'constituencies': constituencies }
#     template = 'views/domestic_workers/employee_registration.html'
#     return render(request, template, context)