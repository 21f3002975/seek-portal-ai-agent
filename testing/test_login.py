import requests
import pytest
import json
from globals import verify_keys, assertEquals, assertInstance

API_LOGIN = "https://api-deepseek.vercel.app/login"

headers = {
  'Content-Type': 'application/json'
}

def test_1_student_login(student_mail, 
                         student_name, 
                         profile_picture,
                         login_success_msg,
                         helpers):
    input_data = {
        "email": student_mail,
        "name": student_name,
        "picture": profile_picture
    }
    payload = json.dumps(input_data)

    response = requests.post(API_LOGIN, data=payload, headers=headers)

    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)

    required_keys = {"userId":str, 
                     "name":str, 
                     "email":str, 
                     "role":str, 
                     "message":str, 
                     "picture":str}
    verify_keys(required_keys, data)

    assertEquals(data['email'], student_mail)

    assertEquals(data['message'], login_success_msg)

    assertEquals(data['role'], "student")

def test_2_admin_login(admin_mail,
                       admin_name,
                       profile_picture,
                       login_success_msg):
    input_data = {
    "email": admin_mail,
    "name": admin_name,
    "picture": profile_picture
    }
    payload = json.dumps(input_data)

    response = requests.post(API_LOGIN, data=payload, headers=headers)

    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)

    required_keys = {"userId":str,
                     "name":str, 
                     "email":str, 
                     "role":str, 
                     "message":str, 
                     "picture":str}
    verify_keys(required_keys, data)

    assertEquals(data['email'], admin_mail)

    assertEquals(data['message'], login_success_msg)

    assertEquals(data['role'], "admin")

def test_3_faculty_login(faculty_mail,
                         faculty_name,
                         profile_picture,
                         login_success_msg):
    input_data = {
    "email": faculty_mail,
    "name": faculty_name,
    "picture": profile_picture
    }
    payload = json.dumps(input_data)

    response = requests.post(API_LOGIN, data=payload, headers=headers)

    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)

    required_keys = {"userId":str, 
                     "name":str, 
                     "email":str, 
                     "role":str, 
                     "message":str, 
                     "picture":str}
    verify_keys(required_keys, data)

    assertEquals(data['email'], faculty_mail)

    assertEquals(data['message'], login_success_msg)

    assertEquals(data['role'], "faculty")

def test_4_email_required(student_name,
                          profile_picture,
                          email_required_msg):
    input_data = {
    "email": "",
    "name": student_name,
    "picture": profile_picture
    }
    payload = json.dumps(input_data)

    response = requests.post(API_LOGIN, data=payload, headers=headers)

    assertEquals(response.status_code, 400)
    
    data = response.json()

    required_keys = {"error":str}
    verify_keys(required_keys, data)
    
    assertEquals(data['error'], email_required_msg)

if __name__ == "__main__":
    pytest.main()
