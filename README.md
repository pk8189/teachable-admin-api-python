
# teachable-public-api Python SDK

## Overview
The documentation for the Teachable Public API. All endpoints are currently
subject to change.

## Initilization
Initialize either the synchronous or asynchronous client to authenticate

### Synchronous Client
```python
from teachable_public_api import Client
from os import getenv

Client(api_key=getenv("API_KEY"))
```

### Asynchronous Client
```python
from teachable_public_api import AsyncClient
from os import getenv

AsyncClient(api_key=getenv("API_KEY"))
```


### 
> Fetch all courses at your school.

```python
client.v1.courses.list(
    author_bio_id=123,
    created_at="1970-01-01T00:00:00",
    is_published=True,
    name="string",
    page=123,
    per=123,
)
```

---

### 
> Fetch a specific course by ID.

```python
client.v1.courses.get(course_id=123)
```

---

### 
> Fetch active enrolled students and student progress for a specific course.

```python
client.v1.courses.enrollments.list(
    course_id=123,
    enrolled_in_after="1970-01-01T00:00:00",
    enrolled_in_before="1970-01-01T00:00:00",
    sort_direction="asc",
)
```

---

### 
> Fetch content of a specific course lecture.

```python
client.v1.courses.lectures.get(course_id=123, lecture_id=123)
```

---

### 
> Fetch an id list of quizzes in a specific course lecture.

```python
client.v1.courses.lectures.quizzes.list(course_id=123, lecture_id=123)
```

---

### 
> Fetch a specific quiz information.

```python
client.v1.courses.lectures.quizzes.get(course_id=123, lecture_id=123, quiz_id=123)
```

---

### 
> Fetch the responses of quiz.

```python
client.v1.courses.lectures.quizzes.responses.list(
    course_id=123, lecture_id=123, quiz_id=123
)
```

---

### 
> Fetch a specific video information.

```python
client.v1.courses.lectures.videos.get(
    course_id=123, lecture_id=123, video_id=123, user_id=123
)
```

---

### 
> Fetch a specific user's course progress.

```python
client.v1.courses.progress.list(course_id=123, user_id=123, page=123, per=123)
```

---

### 
> Fetch all the pricing plans at your school

```python
client.v1.pricing_plans.list(page=123, per=123)
```

---

### 
> Fetch details of a specific pricing plan. Currently only supports pricing plans associated with courses.

```python
client.v1.pricing_plans.get(pricing_plan_id=123)
```

---

### 
> Fetch a list of sales transactions made in your school. (New transactions can take up to two minutes to be returned via API call from the time of sale.)

```python
client.v1.transactions.list(
    affiliate_id=123,
    course_id=123,
    end="1970-01-01T00:00:00",
    is_chargeback=True,
    is_fully_refunded=True,
    page=123,
    per=123,
    pricing_plan_id=123,
    start="1970-01-01T00:00:00",
    user_id=123,
)
```

---

### 
> Get a list of users

```python
client.v1.users.list(email_query="string", page=123, per=123)
```

---

### 
> List a specific user and their course enrollments by user ID.

```python
client.v1.users.get(user_id=123)
```

---

### 
> Fetch all webhook events for your school.

```python
client.v1.webhooks.list()
```

---

### 
> Fetch all the events for a webhook.

```python
client.v1.webhooks.events.list(
    webhook_id=123,
    created_after="1970-01-01T00:00:00",
    created_before="1970-01-01T00:00:00",
    page=123,
    per=123,
    response_http_status_gte=123,
    response_http_status_lte=123,
)
```

---

### 
> Update the name or src of a user.

```python
client.v1.users.patch(user_id=123, data={"name": "string", "src": "string"})
```

---

### 
> Mark a specific course lecture as complete.

```python
client.v1.courses.lectures.mark_complete.create(
    course_id=123, lecture_id=123, data={"user_id": 123}
)
```

---

### 
> Enroll a user in a course.

```python
client.v1.enroll.create(data={"course_id": 123, "user_id": 123})
```

---

### 
> Unenroll a user from a course.

```python
client.v1.unenroll.create(data={"course_id": 123, "user_id": 123})
```

---

### 
> Create a new user

```python
client.v1.users.create(
    data={
        "email_field": "string",
        "name": "string",
        "password": "string",
        "src": "string",
    }
)
```


