# Chatbot API Test Documentation

## Test 1: Chatbot Interaction

**API URL:** `https://api-deepseek.vercel.app/chatbot`  
**API Method:** `POST`  

### Input Data:
```json
{
    "query": "What is ML?",
    "option": "option",
    "sessionId": "S1234",
    "userEmail": "student_mail"
}
```

### Expected Status Code:
`200`

### Actual Status Code:
`200`

### Expected Keys and Data Types in Response:
- `sessionId` : `str`
- `question` : `str`
- `answer` : `str`
- `chatHistory` : `list`

### Actual Keys and Data Types in Response:
- `sessionId` : `str`
- `question` : `str`
- `answer` : `str`
- `chatHistory` : `list`

## Additional Data Verification

### Chat History Structure:

Each item in the `chatHistory` list must contain:
- `query` : `str`
- `answer` : `str`
- `timestamp` : `str`
- `user` : `dict`

### User Structure:

Each `user` object in the `chatHistory` must contain:
- `id` : `str`
- `name` : `str`
- `email` : `str`
- `role` : `str`
- `profilePictureUrl` : `str`

### Python Code:
```

def test_1_chatbot(student_mail,
                 student_id,
                 student_name,
                 student_pp):
    session_id = "S1234"
    query = "What is ML?"
    input_data = {
        "query": query,
        "option": "option",
        "sessionId": session_id,
        "userEmail": student_mail
    }
    payload = json.dumps(input_data)

    response = requests.post(API_CHATBOT, data=payload, headers=headers)

    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)
    
    required_keys = {"sessionId":str, 
                        "question":str, 
                        "answer":str, 
                        "chatHistory": list
                    }
    verify_keys(required_keys, data)

    assertEquals(data['sessionId'], session_id)

    assertEquals(data['question'], query)

    chathistories = data["chatHistory"]
    for chathistory in chathistories:
        assertInstance(chathistory, dict)
        
        required_keys = {"query":str, 
                            "answer":str, 
                            "timestamp":str, 
                            "user": dict
                        }
        verify_keys(required_keys, chathistory)

        user = chathistory['user']
        required_keys = {"id":str, 
                            "name":str, 
                            "email":str, 
                            "role": str,
                            "profilePictureUrl": str
                        }
        verify_keys(required_keys, user)

        assertEquals(user['name'], student_name)

        assertEquals(user['email'], student_mail)

        assertEquals(user['role'], "student")

        assertEquals(user['profilePictureUrl'], student_pp)
```
---

## Test 2: Incomplete Payload

**API URL:** `https://api-deepseek.vercel.app/chatbot`  
**API Method:** `POST`  

### Input Data:
```json
{
    "option": "option",
    "sessionId": "S1234",
    "userEmail": "student_mail"
}
```

### Expected Status Code:
`400`

### Actual Status Code:
`400`

### Expected Error Message:
`Query and option are required`

### Actual Error Message:
`Query and option are required`

### Expected Keys and Data Types in Response:
- `error` : `str`

### Actual Keys and Data Types in Response:
- `error` : `str`

### Python Code:
```

def test_2_incomplete_payload(student_mail,
                                    query_option_required_msg):
    input_data = {
        "option": "option",
        "sessionId": "S1234",
        "userEmail": student_mail
    }
    payload = json.dumps(input_data)

    response = requests.post(API_CHATBOT, data=payload, headers=headers)

    assertEquals(response.status_code, 400)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)
    
    required_keys = {"error":str}
    verify_keys(required_keys, data)

    assertEquals(data['error'], query_option_required_msg)
```
---

## Test 3: Invalid User

**API URL:** `https://api-deepseek.vercel.app/chatbot`  
**API Method:** `POST`  

### Input Data:
```json
{
    "query": "What is ML?",
    "option": "option",
    "sessionId": "S1234",
    "userEmail": "invalid_student_mail"
}
```

### Expected Status Code:
`404`

### Actual Status Code:
`404`

### Expected Error Message:
`User not found`

### Actual Error Message:
`User not found`

### Expected Keys and Data Types in Response:
- `error` : `str`

### Actual Keys and Data Types in Response:
- `error` : `str`

### Python Code:
```

def test_3_invalid_user(invalid_student_mail,
                           user_not_found_msg):
    input_data = {
        "query": "What is ML?",
        "option": "option",
        "sessionId": "S1234",
        "userEmail": invalid_student_mail
    }
    payload = json.dumps(input_data)

    response = requests.post(API_CHATBOT, data=payload, headers=headers)

    assertEquals(response.status_code, 404)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)
    
    required_keys = {"error":str}
    verify_keys(required_keys, data)

    assertEquals(data['error'], user_not_found_msg)
```
---
