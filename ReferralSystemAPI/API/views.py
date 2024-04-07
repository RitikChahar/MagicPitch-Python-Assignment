from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from .forms import UserForm, ReferralForm
from .models import User
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
                    })
            if user_form.is_valid():
                user_form.save()
                return JsonResponse ({
                    "success":True,
                    "message":"Registration Successful.",
                    "user_id":user_id
                    })
            else:
                return JsonResponse({
                    "success":False,
                    "message":"Form is not valid, check if any field is missing."
                })
        else:
            return JsonResponse({
                "success":False,
                "message":"Email already exists, try to register with a new email."
            })
    else:
        return HttpResponse("Method Not Allowed")

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
                token = generate_jwt_token(user)
                return JsonResponse ({
                    "success":True,
                    "message":"Login Successful.",
                    "token":token
                    })
            else:
                return JsonResponse ({
                    "success":False,
                    "message":"Wrong Password",
                    })
        else:
            return JsonResponse ({
                "success":False,
                "message":"User does not exist.",
                })
    else:
        return HttpResponse("Method Not Allowed")