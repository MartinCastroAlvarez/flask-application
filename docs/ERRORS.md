# Errors

## Status Codes
This API follows HTTP response codes standards.
*NOTE*: Status codes not listed in this doc are described [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

##### 200 OK
Succesfully messages return a `200 OK` response.
```
200 OK
{
    "people": ...
}
```

##### 400 Bad Request
The request failed because of the client request.
Error subcodes are always provided.
```
400 BAD REQUEST
{
    "errors": {
        4000: "Please insert a valid first name.",
        4001: "Please insert a valid last namename.",
    }
}
```

##### 403 Unauthorized
The request failed because the client is not authorized.
The response body might be empty.
```
403 UNAUTHORIZED
{}
```

##### 404 Not Found
The requested resource doesn't exist.
The response body might be empty.
```
404 NOT FOUND
{}
```

##### 409 Conflict
The resource already exists in the system.
Error subcodes are always provided.
```
409 CONFLICT
{
    "errors": {
        9001: "Alias is already taken."
    }
}

```

## Error Subcodes

##### App Errors (5xxx)
* *5000*: Unexpected Exception.
* *5001*: Method not implemented.
* *5002*: Endpoint not found.

##### Auth Errors (3xxx)
* *3000*: Unexpected Auth error.
* *3001*: Username error.
* *3002*: Password error.

##### Form Errors (4xxx)
* *4000*: Unexpected Form error.
* *4001*: Bad first name.
* *4002*: Bad last name.
* *4003*: Bad alias.
* *4004*: Bad title.
* *4005*: Bad username.
* *4006*: Bad password.
* *4007*: Person Not Found.
* *4008*: Bad Page Number.
* *4009*: Bad Page Limit.
* *4010*: Bad Release Date.
* *4011*: Movie Not found.

##### Conflict Errors (9xxx)
* *9001*: Alias is already taken.
