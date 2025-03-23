# Video Transcript API Test Documentation

## Test 1: Fetch Video Transcript

**API URL:** `https://api-deepseek.vercel.app/video-transcript?videoURL={video_url}`  
**API Method:** `GET`  

### Expected Status Code:
`200`

### Actual Status Code:
`200`

### Expected Keys and Data Types in Response:
- `videoID` : `str`
- `videoURL` : `str`
- `transcript` : `str`

### Actual Keys and Data Types in Response:
- `videoID` : `str`
- `videoURL` : `str`
- `transcript` : `str`

### Python Code:
```

def test_1_transcript_video(video_url):
    response = requests.get(API_URL.format(video_url=video_url))
    
    assertEquals(response.status_code, 200)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)

    required_keys = {"videoID":str, 
                    "videoURL":str, 
                    "transcript":str, 
                    }
    verify_keys(required_keys, data)
```
---

## Test 2: Fetch Transcript for Invalid Video

**API URL:** `https://api-deepseek.vercel.app/video-transcript?videoURL={invalid_video_url}`  
**API Method:** `GET`  

### Expected Status Code:
`404`

### Actual Status Code:
`404`

### Expected Error Message:
`Transcript not found for the given video URL`

### Actual Error Message:
`Transcript not found for the given video URL`

### Expected Keys and Data Types in Response:
- `error` : `str`

### Actual Keys and Data Types in Response:
- `error` : `str`

### Python Code:
```

def test_2_transcript_invalid_video(invalid_video_url,
                                  transcript_not_found_msg):
    response = requests.get(API_URL.format(video_url=invalid_video_url))
    
    assertEquals(response.status_code, 404)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)

    required_keys = {"error":str}
    verify_keys(required_keys, data)

    assertEquals(data['error'], transcript_not_found_msg)
```
---

## Test 3: Fetch Transcript Without Video URL

**API URL:** `https://api-deepseek.vercel.app/video-transcript?videoURL=`  
**API Method:** `GET`  

### Expected Status Code:
`400`

### Actual Status Code:
`400`

### Expected Error Message:
`videoURL is required`

### Actual Error Message:
`videoURL is required`

### Expected Keys and Data Types in Response:
- `error` : `str`

### Actual Keys and Data Types in Response:
- `error` : `str`

### Python Code:
```

def test_3_no_parameters(video_url_required_msg):
    response = requests.get(API_URL.format(video_url=''))
    
    assertEquals(response.status_code, 400)
    
    assertEquals(response.headers["Content-Type"], "application/json")

    data = response.json()
    
    assertInstance(data, dict)

    required_keys = {"error":str}
    verify_keys(required_keys, data)

    assertEquals(data['error'], video_url_required_msg)
```
---
