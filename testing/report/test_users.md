# Users API Test Documentation

## Test 1: List All Users

**API URL:** `https://api-deepseek.vercel.app/users`  
**API Method:** `GET`  

### Expected Status Code:
`200`

### Actual Status Code:
`200`

### Expected Keys and Data Types in Response:
- `id` : `str`
- `name` : `str`
- `email` : `str`
- `role` : `str`
- `profilePictureUrl` : `str`
- `registeredCourses` : `list`

### Actual Keys and Data Types in Response:
- `id` : `str`
- `name` : `str`
- `email` : `str`
- `role` : `str`
- `profilePictureUrl` : `str`
- `registeredCourses` : `list`

### Python Code:
```

def test_list_users():
    response = requests.get(API_URL)
    print(response.headers["Content-Type"])

    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    users = response.json()
    
    assertInstance(users, list)

    for user in users:
        assertInstance(user, dict)
        
        required_keys = {"id":str, 
                         "name":str, 
                         "profilePictureUrl":str, 
                         "registeredCourses":list, 
                         "role":str, 
                         "email":str
                         }
        verify_keys(required_keys, user)
```
---
