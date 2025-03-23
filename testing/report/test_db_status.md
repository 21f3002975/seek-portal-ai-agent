# Database Status API Test Documentation

## Test 1: Check Database Status

**API URL:** `https://api-deepseek.vercel.app/db_status`  
**API Method:** `GET`  

### Expected Status Code:
`200`

### Actual Status Code:
`200`

### Expected Keys and Data Types in Response:
- `status` : `bool`

### Actual Keys and Data Types in Response:
- `status` : `bool`

### Python Code:
```

def test_db_status():
    response = requests.get(API_URL)
    print(response.headers["Content-Type"])

    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)
    
    required_keys = {"status":bool}
    verify_keys(required_keys, data)
```
---