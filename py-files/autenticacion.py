
import requests

h={
    "Content-Type":"application/x-www-form-urlencoded"
}

body={
        "username":"luisbrunno03@gmail.com",
        "password":"Luis@1975",
        "grant_type":"password"
    }

BASE_URL = "http://api.invertironline.com"

requests.post(BASE_URL+"/token", headers=h, data=body).json()
 


