# Course Details

## Test 1: Fetch Course Details

**API URL:** `https://api-deepseek.vercel.app/course/{course_id}`  
**API Method:** `GET`  

### Expected Status Code:
`200`

### Actual Status Code:
`200`

### Expected Keys and Data Types in Response:
- `announcements` : `list`
- `courseId` : `str`
- `name` : `str`
- `description` : `str`
- `startDate` : `str`
- `endDate` : `str`
- `weeks` : `list`

### Actual Keys and Data Types in Response:
- `announcements` : `list`
- `courseId` : `str`
- `name` : `str`
- `description` : `str`
- `startDate` : `str`
- `endDate` : `str`
- `weeks` : `list`

## Additional Data Verification

### Announcements Structure:

Each item in the `announcements` list must contain:
- `announcementId` : `str`
- `date` : `str`
- `message` : `str`

### Weeks Structure:

Each item in the `weeks` list must contain:
- `deadline` : `str`
- `modules` : `list`
- `title` : `str`
- `weekId` : `str`

### Modules Structure:

Each item in the `modules` list must contain:
- `moduleId` : `str`
- `title` : `str`
- `type` : `str`

Optional field (only present in some modules):
- `questions` : `list`

### Questions Structure:

If `questions` key is present in a module, each item in the `questions` list must contain:
- `correctAnswer` : `str`
- `options` : `list`
- `question` : `str`
- `type` : `str`

### Python Code:
```

def test_course_details(course1_id):
    response = requests.get(API_COURSE.format(course_id=course1_id))

    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)
    
    required_keys = {"announcements":list, 
                     "courseId":str,
                     "name":str,
                     "description":str,
                     "startDate":str,
                     "endDate":str,
                     "weeks":list
                     }
    verify_keys(required_keys, data)

    announcements = data['announcements']
   
    for announcement in announcements:
        assertInstance(announcement, dict)

        required_keys = {"announcementId":str,
                         "date":str,
                         "message":str
                         }
        verify_keys(required_keys, announcement)

    weeks = data['weeks']
    for week in weeks:
        assertInstance(week, dict)

        required_keys = {"deadline":str,
                         "modules":list,
                         "title":str,
                         "weekId":str
                         }
        verify_keys(required_keys, week)

        modules = week['modules']
        for module in modules:
            assertInstance(module, dict)

            required_keys = {"moduleId":str,
                             "title":str,
                             "type":str
                             } #url and questions not present in all modules
            verify_keys(required_keys, module)

            if "questions" in module:
                questions = module['questions']
                assertInstance(questions, list)
                
                for question in questions:
                    assertInstance(question, dict)

                    required_keys = {"correctAnswer":str,
                                    #  "hint":str, # Hint can be null sometimes.
                                     "options":list,
                                     "question":str,
                                     "type":str
                                     }
                    verify_keys(required_keys, question)

```
---