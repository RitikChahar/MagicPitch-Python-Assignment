from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator, EmptyPage
from .forms import UserForm, ReferralForm
from .models import User, Referral
from .helper import generate_unique_hash, hash_password, verify_password, generate_jwt_token, verify_jwt_token
import json

@csrf_exempt
def register(request):
    if (request.method=="POST"):
        request_data=json.loads(request.body)
        is_unique = User.objects.filter(email = request_data["email"]).exists() 
        referral = False
        if "referral_code" in request_data:
            referral = True
            referred_by = request_data["referral_code"]
        if(is_unique == False):
            user_id = generate_unique_hash(request_data["name"])
            password = hash_password(request_data["password"])
            request_data["referral_code"] = user_id
            request_data["password"] = password
            user_form = UserForm(request_data)
            if referral == True:
                referral_form = ReferralForm({
                    'referred_by': str(referred_by), 
                    'referred_user': str(user_id), 
                    'referral_points': 100 
                    })
                if referral_form.is_valid():
                    referral_form.save()
                else:
                    return JsonResponse({
                        "success":False,
                        "message":"There is an issue with the referral system.",
                    }, status = 400)
            if user_form.is_valid():
                user_form.save()
                return JsonResponse ({
                    "success":True,
                    "message":"Registration Successful.",
                    "user_id":user_id
                    }, status = 201)
            else:
                return JsonResponse({
                    "success":False,
                    "message":"Form is not valid, check if any field is missing."
                }, status = 422)
        else:
            return JsonResponse({
                "success":False,
                "message":"Email already exists, try to register with a new email."
            }, status = 409)
    else:
        return HttpResponse("Method Not Allowed", status = 405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        email = request_data["email"]
        pwd = request_data["password"]
        if(User.objects.filter(email = email).exists()):
            user = User.objects.get(email = email)
            hashed_password = user.password
            if(verify_password(pwd, hashed_password)):
                token = generate_jwt_token(user.email)
                return JsonResponse ({
                    "success":True,
                    "message":"Login Successful.",
                    "token":token
                    }, status = 201)
            else:
                return JsonResponse ({
                    "success":False,
                    "message":"Wrong Password",
                    }, status = 401)
        else:
            return JsonResponse ({
                "success":False,
                "message":"User does not exist.",
                }, status = 401)
    else:
        return HttpResponse("Method Not Allowed", status = 405)
    
@csrf_exempt 
def details(request):
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        user_id = request.GET.get('user_id')
        token = token.split(" ")[1]
        if token:
            user = verify_jwt_token(token)
            if user:
                user_details = User.objects.get(referral_code = user_id)
                output = {
                    "name": user_details.name,
                    "email": user_details.email,
                    "referral_code": user_details.referral_code,
                    "registration_time": user_details.created_at,
                }
                return JsonResponse({
                    "success":True,
                    "message":"Authentication Successful.",
                    "data": output
                }, status = 200)
            else:
                return JsonResponse({
                    "success":False,
                    "message":"Authentication Failed. Wrong Token."
                }, status = 401)
        else:
            return JsonResponse({
                "success":False,
                "message":"Authentication Failed. Token Missing."
            }, status = 403)
    else:
        return HttpResponse("Method Not Allowed", status = 405)

@csrf_exempt 
def refer(request):
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        page_number = int(request.GET.get('page', 1))
        items_per_page = 20
        referral_code = request.GET.get('referral_code')
        token = token.split(" ")[1]
        if token:
            user = verify_jwt_token(token)
            if user:
                user_details = Referral.objects.filter(referred_by = referral_code)
                paginator = Paginator(user_details, items_per_page)
                try:
                    page_obj = paginator.page(page_number)
                except EmptyPage:
                    page_obj = paginator.page(paginator.num_pages)
                output = []
                for record in page_obj:
                    output.append({
                        "user_id": record.referred_user,
                        "registration_timestamp": record.created_at
                    })
                return JsonResponse({
                    "success":True,
                    "message":"Authentication Successful.",
                    "data": output
                }, status = 200)
            else:
                return JsonResponse({
                    "success":False,
                    "message":"Authentication Failed. Wrong Token."
                }, status = 401)
        else:
            return JsonResponse({
                "success":False,
                "message":"Authentication Failed. Token Missing."
            }, status = 403)
    else:
        return HttpResponse("Method Not Allowed", status = 405)