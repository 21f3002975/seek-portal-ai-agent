# Courses API Test Documentation

## Test 1: List All Courses

**API URL:** `https://api-deepseek.vercel.app/courses`  
**API Method:** `GET`  

### Expected Status Code:
`200`

### Actual Status Code:
`200`

### Expected Keys and Data Types in Response:
- `courses` : `list`

### Actual Keys and Data Types in Response:
- `courses` : `list`

## Additional Data Verification

### Course Structure:

Each item in the `courses` list must contain:
- `id` : `str`
- `name` : `str`
- `description` : `str`
- `startDate` : `str`
- `endDate` : `str`

### Python Code:
```

def test_list_courses():
    response = requests.get(API_URL)
    print(response.headers["Content-Type"])

    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)
    
    courses = data['courses']
    
    assertTrue(len(courses) > 0, "Expected response to contain at least one course")

    assertInstance(courses, list)

    for course in courses:
        assertInstance(course, dict)

        required_keys = {"description":str,
                         "endDate":str,
                         "id":str,
                         "name":str,
                         "startDate":str
                         }
        verify_keys(required_keys, course)
```
---