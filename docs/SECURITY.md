# Penetration Tests

### Setup
Make sure you executed the steps described [here](./INSTALL.md).
You should also follow the setup described [here](./QA.md).

### Authentication Tests

##### Wrong Password Test
```
curl -X POST "${API}/api/v1/auth" -H "Content-Type: application/json" -d '{"username": "1111111111111", "password": "1111111111111"}'
```
Should return:
```
{
  "errors": {
    "3001": "Username not found."
  }
}
```

##### Empty Password Test
```
curl -X POST "${API}/api/v1/auth" -H "Content-Type: application/json" -d '{"username": "1111111111111", "password": ""}'
```
Should return:
```
{
  "errors": {
    "4006": "Password is invalid."
  }
}
```

##### Empty Username Test
```
curl -X POST "${API}/api/v1/auth" -H "Content-Type: application/json" -d '{"username": "", "password": "1111111111"}'
```
Should return:
```
{
  "errors": {
    "4005": "Username is invalid."
  }
}
```

##### Bad Admin Login Test
```
curl -X POST "${API}/api/v1/auth" -H "Content-Type: application/json" -d '{"username": "'${ADMIN_USERNAME}'", "password": "11111111111111"}'
```
Should return:
```
{
  "errors": {
    "3002": "Invalid password."
  }
}
```

##### Admin Login Test
```
curl -c ${COOKIE_JAR} -X POST "${API}/api/v1/auth" -H "Content-Type: application/json" -d '{"username": "'${ADMIN_USERNAME}'", "password": "'${ADMIN_PASSWORD}'"}'
```
Should return:
```
{
  "token": "..."  # A random token is returned.
}
```

##### Wrong Logout Test
```
curl -X DELETE "${API}/api/v1/auth"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

##### Logout Test
```
curl -X DELETE "${API}/api/v1/auth" -b "${COOKIE_JAR}"
```
Should return:
```
{}
```

### People Security Tests

##### Protected Person Creation Test
```
curl -X POST "${API}/api/v1/people"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

##### Protected Person Update Test
```
curl -X PUT "${API}/api/v1/people/1"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

##### Protected Person Deletion Test
```
curl -X DELETE "${API}/api/v1/people/1"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

### Movies Security Tests

##### Protected Movie Creation Test
```
curl -X POST "${API}/api/v1/movies"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

##### Protected Movie Update Test
```
curl -X PUT "${API}/api/v1/movies/1"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

##### Protected Movie Deletion Test
```
curl -X DELETE "${API}/api/v1/movies/1"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

### Actors Security Tests

##### Protected Actor Creation Test
```
curl -X POST "${API}/api/v1/movies/1/actors/1"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

##### Protected Actor Deletion Test
```
curl -X DELETE "${API}/api/v1/movies/1/actors/1"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

### Directors Security Tests

##### Protected Director Creation Test
```
curl -X POST "${API}/api/v1/movies/1/directors/1"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

##### Protected Actor Deletion Test
```
curl -X DELETE "${API}/api/v1/movies/1/directors/1"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

### Producers Security TEsts

##### Protected Producers Creation Test
```
curl -X POST "${API}/api/v1/movies/1/producers/1"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```

##### Protected Actor Deletion Test
```
curl -X DELETE "${API}/api/v1/movies/1/producers/1"
```
Should return:
```
{
  "errors": {
    "3000": "Authentication error."
  }
}
```
