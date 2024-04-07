# MagicPitch-Python-Assignment
The objective of this project is to build a referral system API that allows users to register, view their details, and view their referrals.
## Referral System API Usage
#### For detailed API usage, explore our Postman collection [here](https://documenter.getpostman.com/view/27523601/2sA35MyJi8).
### Base URL
```
http://127.0.0.1:8000
```
### Endpoints
#### 1. Registration Endpoint
#### URL
```/api/register-user/```
#### Method : POST
#### Request
```json
{
    "name":"Ritick Kumar",
    "email":"ritickchahar@gmail.com",
    "password":"WillWorkForMagicPitch",
    "referral_code": "f2824bc23678ea19268ea54bc78a29912a75060c4a1177cc28c4bae368a6ae99"
}
```
#### Response
```json
{
    "success": true,
    "message": "Registration Successful.",
    "user_id": "89fd2f79237a0bdb8ea04878839c288dcec1ebd84987bbacfa0443c28ca66edc"
}
```
#### 2. Login Endpoint
#### URL
```/api/login-user/```
#### Method : POST
#### Request
```json
{
    "email":"ritickchahar@gmail.com",
    "password":"WillWorkForMagicPitch"
}
```
#### Response
```json
{
    "success": true,
    "message": "Login Successful.",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJpdGlja2NoYWhhckBnbWFpbC5jb20iLCJleHAiOjE3MTI2MTczMTd9.TjhIX-eliEW-Wu32x2kV2rhG45R_cVeWhD7sKTHsuuU"
}
```
#### 3. Details Endpoint
#### URL
```/api/get-details/?user_id=<user-id>```
#### Method : GET
#### Header
```json
{
    "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJpdGlja2NoYWhhckBnbWFpbC5jb20iLCJleHAiOjE3MTI2MTczMTd9.TjhIX-eliEW-Wu32x2kV2rhG45R_cVeWhD7sKTHsuuU"
}
```
#### Response
```json
{
    "success": true,
    "message": "Authentication Successful.",
    "data": {
        "name": "Ritick Kumar",
        "email": "ritickchahar@gmail.com",
        "referral_code": "89fd2f79237a0bdb8ea04878839c288dcec1ebd84987bbacfa0443c28ca66edc",
        "registration_time": "2024-04-07T22:59:48.289Z"
    }
}
```
#### 4. Referrals Endpoint
#### URL
```/api/get-referrals/?referral_code=<referrak-code>&page=<page-number>```
#### Method : GET
#### Header
```json
{
    "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJpdGlja2NoYWhhckBnbWFpbC5jb20iLCJleHAiOjE3MTI2MTczMTd9.TjhIX-eliEW-Wu32x2kV2rhG45R_cVeWhD7sKTHsuuU"
}
```
#### Response
```json
{
    "success": true,
    "message": "Authentication Successful.",
    "data": [
        {
            "user_id": "c772de32c6c462a7b655b6f680b7e3ee539cf8dcde6548126238553bfd380843",
            "registration_timestamp": "2024-04-07T22:05:28.714Z"
        },
        {
            "user_id": "7d4595abbd19fecf8cf1d3b769df430ee2584108cb04833bf1f0ef496be8bb18",
            "registration_timestamp": "2024-04-07T22:05:46.427Z"
        }
    ]
}
```