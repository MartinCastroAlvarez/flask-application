# API Interface

### Endpoints

##### Authentication
Some endpoints are protected. Only users sending a request with the token may gain access.
After authenticating, please attach the token to the `session` cookie in your subsequent requets.
Otherwise, you will get a `403 UNAUTHORIZED` error.

###### Login
```
POST /api/v1/users/auth
{
    "username": "lorem",
    "password": "ipsum"
}
```
If credentials are valid:
```
200 OK
{
    "token": "19823ha98spfd98ha9dshf9haf98asdf98ads",
}
```
If credentials are invalid:
```
400 BAD REQUEST
{
    "errors": {
        "3001": "User not found.",
        "3002": "Invalid password."
    }
}
```

###### Logout
```
DELETE /api/v1/users/auth
{}
```
```
200 OK
{}
```

##### People

###### List all People
```
GET /api/v1/people
```
```
{
    "people": [{
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ],
        "movies": {
            "actor": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "is_active": true,
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
            "director": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "is_active": true,
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
            "producer": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "is_active": true,
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
        }
    }]
}
```

###### Get Person by ID
```
GET /api/v1/people/1
```
```
{
    "person": {
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ],
        "movies": {
            "actor": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "is_active": true,
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
            "director": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "is_active": true,
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
            "producer": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "is_active": true,
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
        }
    }
}
```

###### Create Person
```
POST /api/v1/people
{
    "first_name": "Lorem",
    "last_name": "Ipsum",
    "is_active": true,
    "aliases": [
        "test+1@test.com",
        "test+2@test.com",
        "test+3@test.com"
    ]
}
```
```
{
    "person": {
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ],
        "movies": {,
            "actor": [],
            "director": [],
            "producer": []
        }
    }
}
```

###### Update Person
The object is NOT overriden. Hence, this is also a partial update.
```
PUT /api/v1/people/1
{
    "first_name": "Lorem",
    "last_name": "Ipsum",
    "is_active": true,
    "aliases": [
        "test+1@test.com",
        "test+2@test.com",
        "test+3@test.com"
    ]
}
}
```
```
{
"person": {
    "id": 1,
    "first_name": "Lorem",
    "last_name": "Ipsum",
    "is_active": true,
    "aliases": [
        "test+1@test.com",
        "test+2@test.com",
        "test+3@test.com"
    ],
    "movies": {,
        "actor": [{
            "id": 1,
            "title": "Lorem Ipsum",
            "release": {
                "year": 2015,
                "roman": "MMXV"
            }
        }],
        "director": [{
            "id": 1,
            "title": "Lorem Ipsum",
            "release": {
                "year": 2015,
                "roman": "MMXV"
            }
        }],
        "producer": [{
            "id": 1,
            "title": "Lorem Ipsum",
            "release": {
                "year": 2015,
                "roman": "MMXV"
            }
        }]
    }
}
```

###### Delete Person
```
DELETE /api/v1/people/1
```
```
200 OK
{}
```
Subsequent requests to retrieve this object will return:
```
404 NOT FOUND
{}
```

###### Add Person to Movie as Actor
```
POST /api/v1/people/1/movies/actors/1
```
```
{
    "person": {
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ],
        "movies": {,
            "actor": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
            "director": [],
            "producer": [],
        }
    }
}
```

###### Remove Person from Movie as Actor
```
DELETE /api/v1/people/1/movies/actors/1
```
```
{
    "person": {
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ],
        "movies": {,
            "actor": [],
            "director": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
            "producer": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }]
        }
    }
}
```

###### Add Person to Movie as Producer
```
POST /api/v1/people/1/movies/producers/1
```
```
{
    "person": {
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ],
        "movies": {,
            "actor": [],
            "director": [],
            "producer": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }]
        }
    }
}
```

###### Remove Person from Movie as Producer
```
DELETE /api/v1/people/1/movies/producers/1
```
```
{
    "person": {
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ],
        "movies": {,
            "actor": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
            "director": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }]
            "producer": []
        }
    }
}
```

###### Add Person to Movie as Director
```
POST /api/v1/people/1/movies/directors/1
```
```
{
    "person": {
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ],
        "movies": {,
            "actor": [],
            "director": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
            "producer": [],
        }
    }
}
```

###### Remove Person from Movie as Director
```
DELETE /api/v1/people/1/movies/directors/1
```
```
{
    "person": {
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ],
        "movies": {,
            "actor": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }],
            "director": [],
            "producer": [{
                "id": 1,
                "title": "Lorem Ipsum",
                "release": {
                    "year": 2015,
                    "roman": "MMXV"
                }
            }]
        }
    }
}
```

##### Movie

###### List all Movies
```
GET /api/v1/movies
```
```
{
    "movies": [{
        "id": 1,
        "title": "Lorem Ipsum",
        "is_active": true,
        "release": {
            "year": 2015,
            "roman": "MMXV"
        },
        "actors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "directors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "producers": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }]
    }]
}
```

###### Get Movie by ID
```
GET /api/v1/movies/1
```
```
{
    "movie": {
        "id": 1,
        "title": "Lorem Ipsum",
        "is_active": true,
        "release": {
            "year": 2015,
            "roman": "MMXV"
        },
        "actors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "directors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "producers": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }]
    }
}
```

###### Create Movie
```
POST /api/v1/movies
{
    "title": "Lorem Ipsum",
    "is_active": true,
    "release_at": "2019-01-01"
}
```
```
{
    "movie": {
        "id": 1,
        "title": "Lorem Ipsum",
        "is_active": true,
        "release": {
            "year": 2015,
            "roman": "MMXV"
        },
        "actors": [],
        "directors": [],
        "producers": [],
    }
}
```

###### Update Movie
The object is NOT overriden. Hence, this is also a partial update.
```
PUT /api/v1/movies
{
    "title": "Lorem Ipsum",
    "is_active": true,
    "released_at": "2019-01-01"
}
```
```
{
"movie": {
    "id": 1,
    "title": "Lorem Ipsum",
    "is_active": true,
    "release": {
        "year": 2015,
        "roman": "MMXV"
    },
    "actors": [{
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ]
    }],
    "directors": [{
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ]
    }],
    "producers": [{
        "id": 1,
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "is_active": true,
        "aliases": [
            "test+1@test.com",
            "test+2@test.com",
            "test+3@test.com"
        ]
    }]
}
}
```

###### Delete Movie
```
DELETE /api/v1/movie/1
```
```
200 OK
{}
```
Subsequent requests to retrieve this object will return:
```
404 NOT FOUND
{}
```

###### Add Actor to Movie
```
POST /api/v1/movies/1/actors/1
```
```
{
    "movie": {
        "id": 1,
        "title": "Lorem Ipsum",
        "is_active": true,
        "release": {
            "year": 2015,
            "roman": "MMXV"
        },
        "actors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "directors": [],
        "producers": [],
    }
}
```

###### Remove Actor from Movie
```
DELETE /api/v1/movies/1/actors/1
```
```
{
    "movie": {
        "id": 1,
        "title": "Lorem Ipsum",
        "is_active": true,
        "release": {
            "year": 2015,
            "roman": "MMXV"
        },
        "actors": [],
        "directors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "producers": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }]
    }
}
```

###### Add Producer to Movie
```
POST /api/v1/movies/1/producers/1
```
```
{
    "movie": {
        "id": 1,
        "title": "Lorem Ipsum",
        "is_active": true,
        "release": {
            "year": 2015,
            "roman": "MMXV"
        },
        "actors": [],
        "directors": [],
        "producers": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }]
    }
}
```

###### Remove Producer from Movie
```
DELETE /api/v1/movies/1/producers/1
```
```
{
    "movie": {
        "id": 1,
        "title": "Lorem Ipsum",
        "is_active": true,
        "release": {
            "year": 2015,
            "roman": "MMXV"
        },
        "actors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "directors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "producers": [],
    }
}
```

###### Add Director to Movie
```
POST /api/v1/movies/1/directors/1
```
```
{
    "movie": {
        "id": 1,
        "title": "Lorem Ipsum",
        "is_active": true,
        "release": {
            "year": 2015,
            "roman": "MMXV"
        },
        "actors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "directors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "producers": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }]
    }
}
```

###### Remove Director from Movie
```
DELETE /api/v1/movies/1/directors/1
```
```
{
    "movie": {
        "id": 1,
        "title": "Lorem Ipsum",
        "is_active": true,
        "release": {
            "year": 2015,
            "roman": "MMXV"
        },
        "actors": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }],
        "directors": [],
        "producers": [{
            "id": 1,
            "first_name": "Lorem",
            "last_name": "Ipsum",
            "is_active": true,
            "aliases": [
                "test+1@test.com",
                "test+2@test.com",
                "test+3@test.com"
            ]
        }]
    }
}
```
