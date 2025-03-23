## Test: Admin Statistics

**API URL:** `https://api-deepseek.vercel.app/admin-statistics`  
**API Method:** `GET`  

### Expected Status Code:

`200`

### Actual Status Code:

`200`

### Expected Keys and Data Types in Response:

- `totalUsers` : `int`
- `totalModules` : `int`
- `activeUsers` : `int`
- `questionsAttempted` : `int`

### Actual Keys and Data Types in Response:

- `totalUsers` : `int`
- `totalModules` : `int`
- `activeUsers` : `int`
- `questionsAttempted` : `int`

### Python Code:
```

def test_admin_statistics():
    response = requests.get(API_URL)
    print(response.headers["Content-Type"])

    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)
    
    required_keys = {"totalUsers":int,
                        "totalModules":int,
                        "activeUsers":int,
                        "questionsAttempted":int
                    }
    verify_keys(required_keys, data)
```
---