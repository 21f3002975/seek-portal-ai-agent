# User Statistics API Test Documentation

## Test 1: User Login

**API URL:** `https://api-deepseek.vercel.app/login`  
**API Method:** `POST`  

### Input Data:
```json
{
    "email": "student2_mail",
    "name": "student2_name",
    "picture": "profile_picture"
}
```

### Expected Status Code:
`200`

### Actual Status Code:
`200`

### Expected Keys and Data Types in Response:
- `userId` : `str`

### Actual Keys and Data Types in Response:
- `userId` : `str`

### Python Code:
```

def test_1_login(student2_name,
                 student2_mail,
                 profile_picture):
    global user_id 
    input_data = {
        "email": student2_mail,
        "name": student2_name,
        "picture": profile_picture
    }
    payload = json.dumps(input_data)

    response = requests.post(API_LOGIN, data=payload, headers=headers)

    assertEquals(response.status_code, 200)
    
    data = response.json()
    
    user_id = data['userId']
```
---

## Test 2: Fetch User Statistics

**API URL:** `https://api-deepseek.vercel.app/user-statistics/{user_id}`  
**API Method:** `GET`  

### Expected Status Code:
`200`

### Actual Status Code:
`200`

### Expected Keys and Data Types in Response:
- `id` : `str`
- `name` : `str`
- `email` : `str`
- `statistics` : `dict`
- `registeredCourses` : `list`
- `role` : `str`

### Actual Keys and Data Types in Response:
- `id` : `str`
- `name` : `str`
- `email` : `str`
- `statistics` : `dict`
- `registeredCourses` : `list`
- `role` : `str`

## Additional Data Verification

### Statistics Structure:

Each `statistics` object must contain:
- `averageScore` : `int`
- `modulesCompleted` : `int`
- `questionsAttempted` : `int`

### Python Code:
```

def test_2_user_statistics():
    global user_id 
    response = requests.get(API_USER_STATS.format(user_id=user_id))

    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)

    required_keys = {"id":str,
                     "name":str, 
                     "email":str, 
                     "statistics":dict, 
                     "registeredCourses":list, 
                     "role":str
                     }
    verify_keys(required_keys, data)

    statistics = data['statistics']    

    required_keys = {"averageScore":int, 
                     "modulesCompleted":int, 
                     "questionsAttempted":int
                     }
    verify_keys(required_keys, statistics)

    assertEquals(data['id'], user_id)

    assertEquals(data['role'], "student")
```
---

## Test 3: Delete User

**API URL:** `https://api-deepseek.vercel.app/user/{user_id}`  
**API Method:** `DELETE`  

### Expected Status Code:
`200`

### Actual Status Code:
`200`

### Expected Message:
`User deleted successfully`

### Actual Message:
`User deleted successfully`

### Expected Keys and Data Types in Response:
- `message` : `str`

### Actual Keys and Data Types in Response:
- `message` : `str`

### Python Code:
```

def test_3_user_delete(user_del_success_msg):
    global user_id 
    response = requests.delete(API_USER.format(user_id=user_id))

    data = response.json()
    
    required_keys = ["message"]
    assertTrue(set(required_keys) == set(data.keys()), f"Expected response to have following keys: {required_keys}, but found the following keys: {list(data.keys())}")

    assertEquals(data['message'], user_del_success_msg)
```
---

## Test 4: Fetch Statistics for Non-Existent User

**API URL:** `https://api-deepseek.vercel.app/user-statistics/{user_id}`  
**API Method:** `GET`  

### Expected Status Code:
`404`

### Actual Status Code:
`404`

### Expected Error Message:
`Internal Server Error`

### Actual Error Message:
`Internal Server Error`

### Expected Keys and Data Types in Response:
- `message` : `str`

### Actual Keys and Data Types in Response:
- `message` : `str`

### Python Code:
```

def test_4_user_statistics_user_not_found(server_error_msg):
    global user_id 
    response = requests.get(API_USER_STATS.format(user_id=user_id))

    assertEquals(response.status_code, 404) # Bug
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)

    required_keys = {"message":str}
    verify_keys(required_keys, data)

    assertEquals(data['message'], server_error_msg)
```
---